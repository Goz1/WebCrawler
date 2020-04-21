# -*- coding: utf-8 -*-
from selenium import webdriver
import time
import csv
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

links = []
attributes = []
count = 0


# Download metadata from Google Play
# read the file with all the links and input them into the driver individually
with open('appLinks.txt', 'r') as f:
    links = f.read().splitlines()

for link in links:
    driver.get(link)

    # App name
    attributes.append(driver.find_element(By.XPATH, '//div[@class="sIskre"]//h1[@class="AHFaub"]').text)

    # Category
    attributes.append(driver.find_elements_by_xpath('//div[@class="sIskre"]//div[@class="qQKdcc"]//span[@class="T32cc UAO9ie"]')[1].text)

    # Size
    attributes.append(driver.find_elements(By.XPATH,'//div[@class="W4P4ne "]//div[@class="IQ1z0d"]//span[@class="htlgb"]')[1].text)

    # Ratings
    attributes.append(driver.find_elements(By.XPATH,'//div[@class="K9wGie"]')[0].text)

    # Developers
    attributes.append(driver.find_elements(By.XPATH, '//div[@class="sIskre"]//div[@class="qQKdcc"]//span[@class="T32cc UAO9ie"]')[0].text)

    # No of installations
    attributes.append(driver.find_elements(By.XPATH, '//div[@class="W4P4ne "]//div[@class="hAyfc"]//div[@class="IQ1z0d"]')[2].text)

    # Policy
    # attributes.append(link to policy)

    # Developer(s) Website
    # attributes.append(Developers' website)


    # Permissions
    windows_before = driver.window_handles[0]
    driver.find_element_by_link_text("View details").click()
    time.sleep(1)
    windows_after = driver.window_handles[-1]
    driver.switch_to.window(windows_after)
    permissions = driver.find_elements_by_xpath('//html//span[@class="PbnGhe oJeWuf fb0g6 Pq2lFf"]//li[@class="BCMWSd"]')
    for permission in permissions:
        attributes.append(permission.text)
    count += 1
    print(count)

driver.close()

# Save scapped attributes in csv file
with open('tempDataset.csv', 'w', newline='', encoding="utf-8") as f:
    thewriter = csv.writer(f)
    thewriter.writerow(['App_Name', 'Category', 'Size', 'Ratings', 'Developers', 'No_of_installs', 'Permissions'])
    thewriter.writerow(attributes)
f.close()


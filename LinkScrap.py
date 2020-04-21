# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

# Google Play Store link path to be scrubbed for information
# Categories to download from:

# Games
driver.get('https://play.google.com/store/apps/collection/cluster?clp=SiwKKgokcHJvbW90aW9uXzMwMDA3OTFfbmV3X3JlbGVhc2VzX2dhbWVzEAcYAw%3D%3D:S:ANO1ljJAzZo&gsr=Ci5KLAoqCiRwcm9tb3Rpb25fMzAwMDc5MV9uZXdfcmVsZWFzZXNfZ2FtZXMQBxgD:S:ANO1ljIA02c&hl=en_US')

# Dating:
driver.get('https://play.google.com/store/apps/collection/cluster?clp=0g4eChwKFnRvcHNlbGxpbmdfZnJlZV9EQVRJTkcQBxgD:S:ANO1ljJ0qxs&gsr=CiHSDh4KHAoWdG9wc2VsbGluZ19mcmVlX0RBVElORxAHGAM%3D:S:ANO1ljJvMRw&hl=en_US')

# Social:
driver.get('https://play.google.com/store/apps/category/SOCIAL?hl=en_US')

# Shopping:
driver.get('https://play.google.com/store/apps/category/SHOPPING?hl=en_US')

# Music
driver.get('https://play.google.com/store/apps/category/MUSIC_AND_AUDIO?hl=en_US')

# Entertainment
driver.get('https://play.google.com/store/apps/category/ENTERTAINMENT')



# Path to extract information from
extraLinks = driver.find_elements_by_xpath("//div[@class='b8cIId ReQCgd Q9MA7b']/a")


# Save links in list
count = 0
myList = []
for item in extraLinks:
    my_href = item.get_attribute('href')
    myList.append(my_href)
    count += 1
print('There are ', count, 'number of apps gotten from the link')
driver.close()


# Get links from list and save to file
with open('applinks.txt', 'w') as f:
    for i in myList:
        f.write(i)
        f.write("\n")
f.close()
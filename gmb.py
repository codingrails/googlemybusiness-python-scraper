from selenium import webdriver
import pandas as pd
import time
from selenium.webdriver.chrome.service import Service
import csv
import sys
import numpy as np
import regex as re
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# instance of Options class allows
# us to configure Headless Chrome
options = Options()

# this parameter tells Chrome that
# it should be run without UI (Headless)
options.headless = True

driver = webdriver.Chrome(ChromeDriverManager().install())

import pandas as pd

pd.options.display.max_rows = 99900

df = pd.read_excel('excel/allinone.xlsx')

selected_urls = df['urls'][~df['urls'].isnull()]
urls = []
for url in selected_urls:
  urls.append(url)
print(urls)

selected_names = df['name'][~df['name'].isnull()]
names = []
for name in selected_names:
  names.append(name)
print(names)

selected_reviews = df['reviews'][~df['reviews'].isnull()]
reviews2 = []
for review in selected_reviews:
  reviews2.append(review)
print(reviews2)

name_list = []
stars_list = []
review_list = []
duration_list = []
gmb_url = []
for url in urls:



    driver.get(url)
    time.sleep(5)

    driver.find_element_by_xpath('//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[7]/div[2]/button').click()
    get_title = driver.title
    time.sleep(5)

    driver.find_element_by_xpath("//*[@data-index='1']").click()

    time.sleep(5)

    SCROLL_PAUSE_TIME = 1

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    number = 0

    while True:
        number = number+1

        # Scroll down to bottom

        ele = driver.find_element_by_xpath('//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]')
        driver.execute_script('arguments[0].scrollBy(0, 5000);', ele)

        # Wait to load page

        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        print(f'last height: {last_height}')

        ele = driver.find_element_by_xpath('//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]')

        new_height = driver.execute_script("return arguments[0].scrollHeight", ele)

        print(f'new height: {new_height}')

        if number == 5000:
            break

        if new_height == last_height:
            break

        print('cont')
        last_height = new_height

    item = driver.find_elements_by_xpath('//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[9]')

    time.sleep(3)


    for i in item:

        button = i.find_elements_by_tag_name('button')
        for m in button:
            if m.text == "More":
                m.click()
        time.sleep(5)

        name = i.find_elements_by_class_name("d4r55")
        stars = i.find_elements_by_class_name("kvMYJc")
        review = i.find_elements_by_class_name("wiI7pd")
        duration = i.find_elements_by_class_name("rsqaWe")

        for j,k,l,p in zip(name,stars,review,duration):
            name_list.append(j.text)
            stars_list.append(p.text)
            review_list.append(k.get_attribute("aria-label"))
            duration_list.append(l.text)
            gmb_url.append(get_title)

review = pd.DataFrame(
    {'name': name_list,
     'rating': stars_list,
     'review': review_list,
     'duration': duration_list,
     'Site Name': gmb_url})

review.to_csv('google_review.csv',index=False)
print(review)


driver.close()
driver.quit()


usernames = []

scraped_reviews2 = []





with open('google_review.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        usernames.append(row["name"])
        scraped_reviews2.append(row["duration"])




reviewmatched = []
matchedname = []
with open('google_review.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:

        duration = str(row["duration"])
        yashi = re.findall(r"\L<words>", duration, words=reviews2)
        if not yashi:
            c = 1
        else:
            reviewmatched.append(yashi[0])
            matchedname.append(usernames[line_count])
        line_count += 1

print(len(reviewmatched))
print(len(matchedname))

for m in reviews2:
    if m in reviewmatched:
        c = 1
    else:
        reviewmatched.append(m)
        matchedname.append("Drop")

print(len(reviewmatched))
print(len(matchedname))

print(reviewmatched)
print(matchedname)


namematch = []
for eachname in names:
    if eachname in usernames:
        namematch.append("Stick")
    else:
        namematch.append("Drop")
print(namematch)

a = np.array(names)
b = np.array(namematch)

df = pd.DataFrame({"Username" : a, "Name Matched" : b})
df.to_excel("namematch.xlsx", index=False)

a = np.array(reviewmatched)
b = np.array(matchedname)

df = pd.DataFrame({"Reviews" : a, "Reviews Matched" : b})
df.to_excel("reviews2match.xlsx", index=False)
print(len(scraped_reviews2))
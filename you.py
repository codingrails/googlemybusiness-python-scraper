import pandas as pd
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

pd.options.display.max_rows = 99900

df = pd.read_excel('excel/allinone.xlsx')

selected_urls = df['urls'][~df['urls'].isnull()]
urls = []
for url in selected_urls:
  urls.append(url)
print(len(urls))

selected_names = df['name'][~df['name'].isnull()]
names = []
for name in selected_names:
  names.append(name)
print(len(names))

selected_reviews = df['reviews'][~df['reviews'].isnull()]
reviews2 = []
for review in selected_reviews:
  reviews2.append(review)

df = pd.read_csv('google_review.csv')
namematches = []
sd = []
businessname = []
for i in range(len(df)):
    if df.iloc[i, 0] in names:
        namematches.append(df.iloc[i, 0])
        sd.append("Stick")
        businessname.append(df.iloc[i, 4])

for n in names:
    if n not in namematches:
        namematches.append(n)
        sd.append("Drop")
        businessname.append("No business match")

a = np.array(namematches)
b = np.array(sd)
c = np.array(businessname)

print(len(namematches))

df = pd.DataFrame({"Name" : a, "Name Match" : b, "Business Name" : c})
df.to_excel("namematches_urls.xlsx", index=False)
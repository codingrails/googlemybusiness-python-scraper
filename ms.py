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

from selenium.webdriver.common.keys import Keys



driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.google.com/maps/place/Dosa+Plaza/@25.4287171,81.9307814,17z/data=!3m1!4b1!4m6!3m5!1s0x39854b36d8d293bf:0x9dbc20170d7ff12f!8m2!3d25.4287171!4d81.9329701!16s%2Fg%2F11r_wq7ltd")


driver.find_element_by_xpath("//*[@id='QA0Szd']/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/div[2]/span[2]/span[1]").click()
time.sleep(5)
driver.find_element_by_xpath('//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[7]/div[2]/button').click()
get_title = driver.title
time.sleep(5)

driver.find_element_by_xpath("//*[@data-index='1']").click()
time.sleep(5)

SCROLL_PAUSE_TIME = 5
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

    if number == 5:
        break

    if new_height == last_height:
        break

    print('cont')
    last_height = new_height

item = driver.find_elements_by_class_name("w8nwRe")
time.sleep(3)


for i in item:
    i.click()
    time.sleep(1)

names = driver.find_elements_by_class_name("d4r55")
for n in names:
    print(n.text)
time.sleep(5)
driver.find_element_by_xpath("//*[@id='QA0Szd']/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[7]/div[1]/div[1]/div[2]/div/button/span").click()
inputs = driver.find_element_by_xpath("//*[@id='QA0Szd']/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[7]/div[1]/div[2]/div/input")
inputs.send_keys('thank you')
inputs.send_keys(Keys.RETURN)


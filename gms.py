from selenium import webdriver
import pandas as pd
import time
from selenium.webdriver.chrome.service import Service
import csv
import sys
import numpy as np
import regex as re

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


driver = webdriver.Chrome(ChromeDriverManager().install())



# URL of website
url = "https://www.google.com/"

# Getting current URL source code
get_title = driver.title

# Printing the title of this URL
# Here it is null string
print(get_title, " ", len(get_title))

# Opening the website
driver.get(url)

# Getting current URL source code
get_title = driver.title

# Printing the title of this URL
print(get_title, "  ", len(get_title))
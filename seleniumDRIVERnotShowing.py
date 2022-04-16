# get website for the ftse 100 historical data: will need to use selenium to control the website to change the time frame to earliest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

options = Options()
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')
path = r"C:\Users\Abdulkadir\Documents\Programming\chromedriver.exe"
driver = webdriver.Chrome(path, options=options)
wait = WebDriverWait(driver, 5)

link = 'https://www.marketwatch.com/investing/index/ukx/download-data?startDate=01/01/2010&endDate=04/15/2022&countryCode=uk'
driver.get(link)

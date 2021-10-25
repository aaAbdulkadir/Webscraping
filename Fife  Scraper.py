from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
import requests

businesses = []
links = []

# open website
path = r"C:\Users\Abdulkadir\Documents\Programming\chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get('https://www.fifechamber.co.uk/about-us/members-directory')

wait = WebDriverWait(driver, 10)
driver.maximize_window()

a = 0
b = 2000

for x in range(1,354):

    business = driver.find_element_by_xpath(f'/html/body/div[1]/div[1]/div/section/div/section/ul/li[{x}]').text
    print(business)
    businesses.append(business)
    
    try:
        link = driver.find_element_by_xpath(f'/html/body/div[1]/div[1]/div/section/div/section/ul/li[{x}]/a')
        print(link.get_attribute('href'))
        links.append(link.get_attribute('href'))
    except:
        print('N/A')
        links.append('N/A')

    
driver.quit()

df = pd.DataFrame({'Businesses': businesses, 'Links': links})
data = df.to_csv(r"C:\Users\Abdulkadir\Documents\Programming\WebScrapeTeasdale\Chambers\Fife Chamber Of Commerce.csv")
print(df)

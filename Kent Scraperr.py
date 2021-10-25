from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
names = []
addresses = []
emails = []
websites = []


for letter in alphabet:
    # open website
    path = r"C:\Users\Abdulkadir\Documents\Programming\chromedriver.exe"
    driver = webdriver.Chrome(path)
    driver.get('https://www.kentinvictachamber.co.uk/find-a-business/')

    wait = WebDriverWait(driver, 10)
    driver.maximize_window()

    search_box = driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[1]/div[2]/div/div/div/form/div[1]/input')
    search_box.click()

    search_box.send_keys(letter)
    search_button = driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[1]/div[2]/div/div/div/form/div[2]/button')
    search_button.click()

    # detail scraping
    a = 0
    b = 0
    x = 1

    true = True
    while true == True:

        try:
            name = driver.find_element_by_xpath(f'/html/body/div[1]/div/div[3]/div[1]/div/div[2]/div/ul/li[{x}]/div[2]/h2/a').text
            print(name)
            names.append(name)
        except:
            name = 'fail'
            names.append('N/A')
        try:
            address = driver.find_element_by_xpath(f'/html/body/div[1]/div/div[3]/div[1]/div/div[2]/div/ul/li[{x}]/div[2]/div[1]').text
            print(address)
            addresses.append(address)
        except:
            address = 'fail'
            addresses.append('N/A')
        try:
            email = driver.find_element_by_xpath(f'/html/body/div[1]/div/div[3]/div[1]/div/div[2]/div/ul/li[{x}]/div[2]/ul/li[1]').text
            print(email)
            emails.append(email)
        except:
            email = 'fail'
            emails.append('N/A')
        try: 
            website = driver.find_element_by_xpath(f'/html/body/div[1]/div/div[3]/div[1]/div/div[2]/div/ul/li[{x}]/div[2]/div[2]/a').text
            print(website)
            websites.append(website)
        except:
            website = 'fail'
            websites.append(website)

        x += 1
        print(x)

        if name == 'fail':
            true = False

        driver.execute_script(f"window.scrollTo({str(a)},{str(b)})")
        b += 500

    print('done')
    driver.quit()
    
df = pd.DataFrame({'Name': names, 'Address': addresses, 'Email': emails, 'Website': websites})
data = df.to_csv(r"C:\Users\Abdulkadir\Documents\Programming\WebScrapeTeasdale\Chambers\Kent Chamber.csv")
print(data)

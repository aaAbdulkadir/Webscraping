# ------------------------------------------------------- IMPORT -------------------------------------------------------
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

# ------------------------------------------------------- GLOBAL VARIABLE ------------------------------------------------

count = 0

# scroll
a = 0
b = 0

names = []
cuisines = []
areas = []
postcodes = []

if __name__ == "__main__":
    # read the postcodes in
    df = pd.read_csv(r"C:\Users\Abdulkadir\Documents\Programming\WebScrapeTeasdale\Completed Code\POSTCODE UK.csv")
    # change the dataframe into a list of postcodes
    df2 = df["Postcode"].to_list()
    
    for loop in df2[0:10]:
        # if post code works
        path = r"C:\Users\Abdulkadir\Documents\Programming\chromedriver.exe"
        driver = webdriver.Chrome(path)
        driver.get('https://deliveroo.co.uk/?utm_source=google&utm_medium=cpc&utm_term=deliveroo&utm_campaign=%2A%2A%5EAcquisition%5ESearch%5EBrand%5EUK%5ELondon%5E%5EExact%5EAPI%5E%5E%5E%5E%5EEN%5EStrategic%5E%C2%A311240584729&utm_loc=9044936&utm_device=c&utm_adposition=&utm_network=g&utm_targetid=kwd-52577441545&gclid=CjwKCAjw4qCKBhAVEiwAkTYsPEKhyFXk8TXpLeWEhNLlVETeIXAyzY5W0qCZqi_g2sfMsX5ed0Ry3hoCddIQAvD_BwE&gclsrc=aw.ds')

        # get to the web page with the restaurants
        wait = WebDriverWait(driver, 10)
        cookies = wait.until(EC.presence_of_element_located((By.ID, 'onetrust-accept-btn-handler')))
        cookies.click()

        search_box = wait.until(EC.presence_of_element_located((By.ID, 'location-search')))
        search_box.click()

        search_box.send_keys(f'{df2[count]}')

        search_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'ccl-cce251427bbe4ec4')))
        search_button.click()

        # now on the restaurant page, extract info
        x = 1

        # case 1: has restaurant
        try:
            
            pop_up = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[8]/div/div/div/div/div/div[2]/span[2]/button/span')))
            pop_up.click()
            
            # case a: view all
            try:
                see_all = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'ccl-cce251427bbe4ec4')))
                actions = ActionChains(driver)
                actions.move_to_element(see_all).perform()
                see_all.click()
                time.sleep(1)
                
                driver.execute_script(f"window.scrollTo({str(0)},{str(0)})") 

                restaurant = True
                while restaurant == True:

                    # has data
                    try:
                        # list of postcodes
                        postcodes.append(df2[count])

                        # list of areas
                        area = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div[1]/div/div[1]/div/div[1]/div[1]/span/button/div/div[2]/div/div/div/div/span').text
                        areas.append(area)
                        print(f'{df2[count]}: {area}')
                        
                        # open
                        try:
                            name = driver.find_element_by_xpath(f'/html/body/div[1]/div/div/div[2]/div/div[2]/div/ul/li[{x}]/div/div/a/span/span[2]/div[2]/ul/li[1]/span/p').text
                            names.append(name)
                            print(name)

                        # closed
                        except :
                            name = driver.find_element_by_xpath(f'/html/body/div[1]/div/div/div[2]/div/div[2]/div/ul/li[{x}]/div/div/a/span/span[2]/div/ul/li[1]/span/p').text
                            names.append(name)
                            print(name)
                            
                        x += 1

                    # no data
                    except:
                        name = 'empty'
                        names.append('N/A')
                        print('N/A')
                        x += 1
                        
                    # cuisines
                    try:
                        print('-------------------------------------------------')
                        
                        # open
                        try:
                            cuisine = driver.find_element_by_xpath(f'/html/body/div[1]/div/div/div[2]/div/div[2]/div/ul/li[{x}]/div/div/a/span/span[2]/div[2]/ul/li[2]').text
                            cuisines.append(cuisine)
                            print(cuisine)

                        # closed
                        except:
                            cuisine = driver.find_element_by_xpath(f'/html/body/div[1]/div/div/div[2]/div/div[2]/div/ul/li[{x}]/div/div/a/span/span[2]/div/ul/li[2]').text
                            cuisines.append(cuisine)
                            print(cuisine)

                    except:
                        cuisine = 'empty'
                        cuisines.append('N/A')
                        print('N/A')
                    

                    b += 200
                    driver.execute_script(f"window.scrollTo({str(a)},{str(b)})") 

                    if name == 'empty' and x > 20:
                        restaurant = False


            # case b: no view all
            except:
                restaurant = True
                while restaurant == True:

                    # has data
                    try:
                        # list of postcodes
                        postcodes.append(df2[count])

                        # list of areas
                        area = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div[2]/div/div/div/div/div/h3').text
                        areas.append(area)
                        print(f'{df2[count]}: {area}')
                        
                        # open
                        try:
                            name = driver.find_element_by_xpath(f'/html/body/div[1]/div/div/div[2]/div/div[2]/div/ul/li[{x}]/div/div/a/span/span[2]/div[2]/ul/li[1]/span/p').text
                            names.append(name)
                            print(name)

                        # closed
                        except :
                            name = driver.find_element_by_xpath(f'/html/body/div[1]/div/div/div[2]/div/div[2]/div/ul/li[{x}]/div/div/a/span/span[2]/div/ul/li[1]/span/p').text
                            names.append(name)
                            print(name)
                            
                        x += 1

                    # no data
                    except:
                        name = 'empty'
                        names.append('N/A')
                        print('N/A')
                        x += 1
                        
                    # cuisines
                    try:
                        print('-------------------------------------------------')
                        
                        # open
                        try:
                            cuisine = driver.find_element_by_xpath(f'/html/body/div[1]/div/div/div[2]/div/div[2]/div/ul/li[{x}]/div/div/a/span/span[2]/div[2]/ul/li[2]').text
                            cuisines.append(cuisine)
                            print(cuisine)

                        # closed
                        except:
                            cuisine = driver.find_element_by_xpath(f'/html/body/div[1]/div/div/div[2]/div/div[2]/div/ul/li[{x}]/div/div/a/span/span[2]/div/ul/li[2]').text
                            cuisines.append(cuisine)
                            print(cuisine)

                    except:
                        cuisine = 'empty'
                        cuisines.append('N/A')
                        print('N/A')

                    b += 500
                    driver.execute_script(f"window.scrollTo({str(a)},{str(b)})")   

                    if name == 'empty' and x > 80:
                        restaurant = False
                
            driver.quit()
            count += 1

        # case 2: has no restaurants
        except:
            print('error1')
            driver.quit()
            count += 1
            
        print('--------------------------------------------------------------------------------------------')
            
        
        
    # pandas
    data = pd.DataFrame({'Postcode': postcodes, 'Area': areas, 'Restaurant': names, 'Cuisines': cuisines})
    dataCSV = data.to_csv(r"C:\Users\Abdulkadir\Documents\Programming\WebScrapeTeasdale\Deliveroo\DeliverooV2\DeliverooV2_0-300.csv")
    print('-----------------------------DONE-----------------------------')
    print(data)

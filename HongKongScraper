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

list_of_restaurants = []
links = []
area = []

if __name__ == "__main__":
   
    # change the dataframe into a list of areas
    df = pd.read_csv(r"C:\Users\Abdulkadir\Documents\Programming\WebScrapeTeasdale\HongKong\HongKong.csv")
    df2 = df['Area'].to_list()
    
    for loop in df2[0:45]:
        # open website
        path = r"C:\Users\Abdulkadir\Documents\Programming\chromedriver.exe"
        driver = webdriver.Chrome(path)
        driver.get('https://www.ubereats.com/hk-en')
        wait = WebDriverWait(driver, 10)

        # find and type postcode in search bar
        search = wait.until(EC.presence_of_element_located((By.ID, 'location-typeahead-home-input')))
        search.click()
        search.send_keys(f'{df2[count]}')
        search_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main-content"]/div[1]/div[2]/div/div[1]/button')))
        actions = ActionChains(driver)
        actions.move_to_element(search_button).perform()
        time.sleep(1)
        search_button.click()

        # working area
        try:
             # has a show more button
            show_more = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/main/div/div[3]/div[2]/div/button')))
            actions = ActionChains(driver)
            actions.move_to_element(show_more).perform()
            show_more.click()

            print(f'----------------------AREA: {loop}----------------------')

            # remove all show more if it has more than one
            condition = True

            while condition == True:
                try:
                    # has addtional show more buttons
                    show_more = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main-content"]/div/div[3]/div[2]/div/button')))
                    actions = ActionChains(driver)
                    actions.move_to_element(show_more).perform()
                    show_more.click()
                except:
                    print('no more show more')
                    condition = False

            # scroll to top
            time.sleep(1)
            driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)

            a = 0
            b = 0

            # collect data for each restaurant
            time.sleep(1)
            x = 1

            restaurant = True
            while restaurant == True:
                 # if restaurant is open
                try:
                    try:
                        card = driver.find_element_by_xpath(f'//*[@id="main-content"]/div/div[3]/div[2]/div/div[2]/div[{x}]/div/a/h3').text
                        list_of_restaurants.append(card)  
                        print(card)

                        link = driver.find_element_by_xpath(f'//*[@id="main-content"]/div/div[3]/div[2]/div/div[2]/div[{x}]/div/a')
                        print(link.get_attribute('href'))
                        links.append(link.get_attribute('href'))
                        
                        area.append(loop)

                        x += 1
                    except:
                        card = 'empty'
                        x += 1

                # if restaurant is closed
                except:
                    try: 
                        card = driver.find_element_by_xpath(f'//*[@id="main-content"]/div/div[3]/div[2]/div/div[2]/div[{x}]/div/a/h3').text
                        list_of_restaurants.append(card)
                        print(card)

                        link = driver.find_element_by_xpath(f'//*[@id="main-content"]/div/div[3]/div[2]/div/div[2]/div[{x}]/div/a')
                        print(link.get_attribute('href'))
                        links.append(link.get_attribute('href'))
                        
                        area.append(loop)

                        x += 1
                    except
                        card = 'empty'
                        x += 1

                b += 100
                driver.execute_script(f"window.scrollTo({str(a)},{str(b)})")

                if x > 30 and card == 'empty':
                    restaurant = False  
        except:
            print('not a working area')

        driver.quit()
        count += 1

    data = pd.DataFrame({'Area': area, 'Restaurant': list_of_restaurants, 'Links': links})
    dataCSV = data.to_csv(r"C:\Users\Abdulkadir\Documents\Programming\WebScrapeTeasdale\HongKong\HKData.csv")
    print('-----------------------------DONE-----------------------------')

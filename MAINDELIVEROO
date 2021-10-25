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

# -------------------------------------G------------------ GLOBAL VARIABLE ------------------------------------------------
count = 0
postcode_count = 2519
city = []
information = []
postcode = []

if __name__ == "__main__":
    # read the postcodes in
    df = pd.read_csv(r"C:\Users\Abdulkadir\Documents\Programming\WebScrapeTeasdale\Completed Code\POSTCODE UK.csv")
    # change the dataframe into a list of postcodes
    df2 = df["Postcode"].to_list()

    for code in df2[0:2]:
        # if post code works
        path = r"C:\Users\Abdulkadir\Documents\Programming\chromedriver.exe"
        driver = webdriver.Chrome(path)
        driver.get('https://deliveroo.co.uk/?utm_source=google&utm_medium=cpc&utm_term=deliveroo&utm_campaign=%2A%2A%5EAcquisition%5ESearch%5EBrand%5EUK%5ELondon%5E%5EExact%5EAPI%5E%5E%5E%5E%5EEN%5EStrategic%5E%C2%A311240584729&utm_loc=9044936&utm_device=c&utm_adposition=&utm_network=g&utm_targetid=kwd-52577441545&gclid=CjwKCAjw4qCKBhAVEiwAkTYsPEKhyFXk8TXpLeWEhNLlVETeIXAyzY5W0qCZqi_g2sfMsX5ed0Ry3hoCddIQAvD_BwE&gclsrc=aw.ds')
        
        # find and type postcode in search bar
        search = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "location-search")))
        search.click()
        search.send_keys(f'{df2[count]}')
        search_button = driver.find_element_by_xpath("//*[contains(text(), 'Search')]")
        search_button.click()


        # valid address
        try:
            # get rid of pop up
            pop_up = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[10]/div/div/div/div/div/div[2]/span[2]/button/span")))
            pop_up.click()
            
            # remove cookies pop up as it is interfering with view all
            time.sleep(1)
            cookies = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[4]/div[2]/div/button")))
            cookies.click()
            
            # scroll to bottom of page and click view all
            wait = WebDriverWait(driver, 10)
            see_all = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div/div/div[2]/div/div[2]/div/ul/li[161]/span/div/span/button/span')))
            actions = ActionChains(driver)
            actions.move_to_element(see_all).perform()

            # number of restaurants in area
            number_of_restaurants = see_all.text.split()[2]  # count of number of restaurants
            print(f'Number of Restaurants: {number_of_restaurants} \n')

            # area
            area = driver.find_element_by_xpath('//*[@id="__next"]/div/div/div[2]/div/div[1]/div/div[1]/div/div[1]/div[1]/span/button/div/div[2]/div/div/div/div/span')
            area_print = area.text
            print(f'{area_print}: {df2[count]}\n')

            see_all.click()

            a = 0
            b = 200

            # scrape info from each restaurant
            for x in range(1, int(number_of_restaurants) + 1):
                info =  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, f'// *[ @ id = "__next"] / div / div / div[2] / div / div[2] / div / ul / li[{x}] / div / div / a / span / span[2]'))).text
                print(f'{x}: {info} \n')
                postcode.append(code)
                information.append(info) 
                city.append(area_print)

                driver.execute_script(f"window.scrollTo({str(a)},{str(b)})")
                a += 200
                b += 200
            
            
            driver.quit()
    
            count += 1
            
        # post code not available
        except:
            postcode.append(code)
            city.append('N/A')
            information.append('N/A')
            driver.quit()
            count += 1

    data = pd.DataFrame({'Postcode': postcode, 'Area': city, 'Information': information})
    dataCSV = data.to_csv(r"C:\Users\Abdulkadir\Documents\Programming\WebScrapeTeasdale\Completed Code\DeliverooData\DeliverooData.csv")
    print(data)

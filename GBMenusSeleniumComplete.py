import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd

# read the file using pandas
df = pd.read_csv(r"C:\Users\Abdulkadir\Documents\Programming\WebScrapeTeasdale\Completed Code\FullGBLIST.csv")

# change the dataframe into a list of postcodes
df2 = df["Postcode"].to_list()

# use selenium to control webbrowser
Path = r"C:\Users\Abdulkadir\Documents\Programming\chromedriver.exe"
Driver = webdriver.Chrome(Path)
Driver.get("https://www.birminghammail.co.uk/whats-on/food-drink-news/postcode-tool-shows-your-streets-15501186")

# your areas favourite takeaway is. Move to the search box by scrolling
element = Driver.find_element_by_tag_name("h5")
actions = ActionChains(Driver)
actions.move_to_element(element).perform()
time.sleep(10)

# initialise arrays
main_fs =[]
main_ps=[]
others_s=[]

for x in df2:
    # find search box
    search = Driver.find_element_by_name("du-search")

    # type in the post code
    search.send_keys(x)
    search.send_keys(Keys.RETURN)
    time.sleep(3)

    # if alert pops up due to outdated post code
    try:
        print(x)
        alert = Driver.switch_to.alert
        alert.accept()
        search.clear()

        # put empty fields in array
        main_f = " "
        main_p = " "
        others = " "

        # empty to empty array
        main_fs.append(main_f)
        main_ps.append(main_p)
        others_s.append(others)

    # post code checks out
    except:
        print(x)
        main_f = Driver.find_element_by_tag_name("h4").text.strip()
        main_p = Driver.find_element_by_class_name("du-description-val").text.strip()
        others = Driver.find_element_by_class_name("du-ranking").text.strip()
        time.sleep(3)

        # Append result to empty array
        main_fs.append(main_f)
        main_ps.append(main_p)
        others_s.append(others)
        search.clear()

Driver.quit()

# create a dataframe with suitable headers and add results into them
final_new = pd.DataFrame({"Postcode":df2, "First": main_fs, "Percent":main_ps, "Others": others_s })
final_new.to_csv(r"C:\Users\Abdulkadir\Documents\Programming\WebScrapeTeasdale\Completed Code\GBMenusDataFrame.csv")
print(final_new)

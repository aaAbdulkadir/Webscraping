from bs4 import BeautifulSoup
import requests
import pandas as pd
import re

details = []
links = []

# 11208
y = 1

df = pd.read_csv(
    r"C:\Users\Abdulkadir\Documents\Programming\WebScrapeTeasdale\Chambers\Surrey data.csv"
)

for link in df['Links'][7000:8000]:

    try:
        url = link
        website = requests.get(url).text
        soup = BeautifulSoup(website, 'lxml')

        detail = soup.find('div', class_='contact-addr').text
        details.append(detail)
        links.append(link)

        print(y)
        y += 1

    except:
        print('did not work')

data = pd.DataFrame({'Links': links, 'Contact Info': details})
data.to_csv(
    r"C:\Users\Abdulkadir\Documents\Programming\WebScrapeTeasdale\Chambers\Surrey info_7000-8000.csv"
)
print(data)

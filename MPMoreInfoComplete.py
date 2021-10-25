import requests
from bs4 import BeautifulSoup
import pandas

root = 'https://www.theyworkforyou.com/mps/'
content = requests.get(root).text
soup = BeautifulSoup(content, 'lxml')

links = []

for link in soup.find_all('a', class_='people-list__person'):
    links.append(link.get('href'))

people = soup.find_all('a', class_="people-list__person")

for person in range(len(people)):
    url_mp = 'https://www.theyworkforyou.com' + links[person]
    website_mp = requests.get(url_mp).text
    soup_mp = BeautifulSoup(website_mp, 'lxml')

    # name
    mp = people[person].find('h2', class_="people-list__person__name").text.strip()

    # Topic of interest
    comma = soup_mp.find_all('ul', class_='comma-list')

    print(mp)
    print(comma[1].text.strip())
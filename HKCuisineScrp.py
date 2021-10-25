from bs4 import BeautifulSoup
import requests
import pandas as pd
import re

# count = 27829

# change the dataframe into a list of areas
df = pd.read_csv(r"C:\Users\Abdulkadir\Documents\Programming\WebScrapeTeasdale\HongKong\ListForCuisines.csv")

cuisines = []
newLink = []
finalCuisines = []

list_of_food = ['Fast food', 'American', 'Cantonese', 'Japanese', 'Italian', 'Burgers', 
                'Desserts', 'Chinese', 'Asian', 
                'Seafood', 'Thai', 'Pizza', 'Vietnamese', 'Indian', 'Asian fusion', 
                'Noodles', 'Western', 'Juice & smoothies', 'Cafe', 'Fruit', 
                'Snacks', 'Grocery', 'Bakery', 'Pasta', 'Malaysian', 'Mixian', 'Mediterranean', 
                'Taiwanese', 'Korean', 'Fried Chicken', 'Bubble tea', 'Hawaiian', 'Coffe & tea',
               'French', 'European', 'Fried Chicken', 'Mexican', 'Wings', 'Tapas', 'Spanish',
               'Middle Eastern', 'Ramen', 'Noodles', 'Cupcakes', 'Vegetarian', 'Salads', 'Gourmets',
               'Eastern European', 'Vegan', 'Healthy', 'Soup', 'Alcohol', 'Japanese-style curry',
               'South East Asian', 'Gourmet', 'British', 'Street food']
y = 1

for link in df['Links'][9000:10000]:
    
    try:
        url = link
        website = requests.get(link).text
        soup = BeautifulSoup(website, 'lxml')

        cuisine = soup.find_all('a')

        for x in cuisine:
            if x.text in list_of_food:
                cuisines.append(x.text)
            else:
                continue

        cuisines = ', '.join(cuisines)
        print(cuisines)
        finalCuisines.append(cuisines)
        print(finalCuisines)
        cuisines = []
        print(y)
        y += 1
        
    except:
        finalCuisines.append('N/A')
    

df2 = df[9000:10000]
print(df2)
df2['Cuisines'] = finalCuisines

print(df2)

dataCSV = df2.to_csv(r"C:\Users\Abdulkadir\Documents\Programming\WebScrapeTeasdale\HongKong\HKDataCuisines.csv")
print('-----------------------------DONE-----------------------------')

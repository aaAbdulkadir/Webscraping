from bs4 import BeautifulSoup
import requests


# loop through all the pages on website
for n in range(1,105):
    # get MP details
    url = f'https://members.parliament.uk/members/commons?SearchText=&PartyId=&Gender=Any&ForParliament=1&ShowAdvanced=true&page={n}'
    website = requests.get(url).text
    soup = BeautifulSoup(website, 'lxml')

    # find out all the cards of individual person
    people = soup.find_all('a', class_='card card-member')

    # find more info on each card/person
    links = []

    for link in soup.find_all('a', class_='card card-member'):
        links.append(link.get('href'))

    # finding all useful properties
    for person in range(len(people)):
        # name
        name = people[person].find('div', class_='primary-info').text.strip()
        # party
        party = people[person].find('div', class_='secondary-info').text.strip()
        # constituency
        constituency = people[person].find('div', class_='indicator indicator-label').text.strip()
        # status
        url_mp = 'https://members.parliament.uk' + links[person]
        website_mp = requests.get(url_mp).text
        soup_mp = BeautifulSoup(website_mp, 'lxml')

        contact_info = soup_mp.find('div', class_='tabs tabs-stacked-md tabs-stacked-md-full-page')
        contact_button = contact_info.find('a').text.strip()

        if contact_button == 'Contact information':
            status = 'Current MP'

            # get contact info
            info = soup_mp.find_all('div', class_='contact-line')

            # get socials
            socials = soup_mp.find_all('div', class_='indicator indicator-label')

            print(f'Name: {name}')
            print(f'Status: {status}')
            print(f'Party: {party}')
            print(f'Constituency: {constituency}')

            # phone/email
            for x in info:
                contact = x.text.strip()
                print(contact)

            # socials
            for x in socials:
                social = x.text.strip()
                print(social)

            print('\n')

        else:
            print(f'Name: {name}')
            status = 'Former MP'
            print(f'Status: {status}')
            print(f'Party: {party}')
            constituency = 'N/A'
            print(f'Constituency: {constituency}')
            contact = 'Phone: N/A\nEmail: N/A'
            print(contact)
            socials = 'Socials: N/A'
            print(socials)
            print('\n')


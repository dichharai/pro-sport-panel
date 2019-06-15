#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

website_content = requests.get('https://en.wikipedia.org/wiki/List_of_NHL_players').text

soup = BeautifulSoup(website_content, 'lxml')

title = soup.title.string.rstrip()
print(f'{title}')
pattern = '='*len(title) + '\n'
print(f'{pattern}')

divs = soup.find_all('div', {'class': 'div-col'})
current_team = divs[0]
lis = current_team.find_all('li')
file = open('nhl-links.txt', 'w+')
file.write(title + '\n')
file.write(pattern + '\n')
for li in lis:
    link = li.a.get('href') + '\n'
    #print(link)
    file.write(link)
    # file.write(print(f'{li.a.get("href")}\n'))
file.close()



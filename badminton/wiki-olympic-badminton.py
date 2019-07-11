#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

website_content = requests.get('https://en.wikipedia.org/wiki/Category:Olympic_badminton_players_of_the_United_States').text

soup = BeautifulSoup(website_content, 'lxml')
# print(soup.prettify())
title = soup.title.string.rstrip()
print(f'{title}')
pat0 = '='*len(title)
print(f'{pat0} \n')

total_players = 0
header = 'Player name'
pat =  '-'*len(header)
print(f'{header}')
print(f'{pat}')


divs = soup.find_all('div', {'class': 'mw-category'})
lis = divs[0].find_all('li')
# print(len(lis))
# print(divs[1])
# print(len(divs))
player_count = 0

for li in lis:
    name = li.a['title'].rstrip()
    print(f'{name}')
    player_count += 1

print(f'\nTotal players: {player_count}')




#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

website_content = requests.get('https://en.wikipedia.org/wiki/Major_League_Soccer#Current').text
soup = BeautifulSoup(website_content, 'lxml')
# print(soup.prettify())
title = soup.title.string.rstrip()
print(f'{title}')
pat0 = '='*len(title)
print(f'{pat0} \n')

table = soup.find_all('table', {'class': 'wikitable'})
# print(len(table))
team_table = table[0]
# print(team_table) # prints table with team name and their links

trs = team_table.find_all('tr')
for i in range(2, len(trs)):
    tr = trs[i]
    print(f'{tr.a["href"]}')
















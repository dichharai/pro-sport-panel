#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

website_content = requests.get('https://en.wikipedia.org/wiki/List_of_current_AFC_team_rosters').text

soup = BeautifulSoup(website_content, 'lxml')
# print(soup.prettify())
title = soup.title.string
print(f'{title}\n')

count = 0

tables = soup.find_all('table', {'class': 'toccolours'})
#print(len(tables))

for table in tables: 
    trs = table.find_all('tr')
    #print(len(trs))
    tr_content = trs[1] # tr with actual data
    tr_uls = tr_content.find_all('ul') # find all uls
    for i in range(len(tr_uls)):
        uls = tr_uls[i]
        lis = uls.find_all('li')
        for li in lis:
            if li.find('span') and li.find('a'):
                print(f'{li.span.string} {li.a.string}')
                count += 1

print(f'Total players: {count}')


# print(soup('span', {'class': "mw-headline"})[0])
'''
tables = soup.find_all('table', {'class': 'toccolours'})
table = tables[0]
trs = (table.find_all('tr'))
tr_content = trs[1]
# print(tr_content) # finding all table content


tr_uls = tr_content.find_all('ul')
# print(tr_uls) # prints all uls containing lis of athletes
#print(len(tr_uls))

for i in range(len(tr_uls)):
    uls = tr_uls[i]
    lis = uls.find_all('li')
    for li in lis:
        if li.find('span') and li.find('a'):
            print(f'{li.span.string} {li.a.string}')


'''
'''
# print(len(tr_uls))
# print(tr_uls[0].find_all('li'))
lis = tr_uls[0].find_all('li')
for li in lis:
    print(f'{li.span.string} {li.a.string}')
'''
'''
for tr in trs:
    print(tr.)

for table in tables:
    print(table.get('tbody'))
'''
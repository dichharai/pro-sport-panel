#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

website_content = requests.get('https://en.wikipedia.org/wiki/List_of_American_Walker_Cup_golfers').text
# print(website_content)

soup = BeautifulSoup(website_content, 'lxml')
# print(soup.prettify())
title = soup.title.string.rstrip()
# writing to a file
write_file_name_list = title.split(' ')
#  print(write_file_name_list)

w_file_name = 'american-walker-cup-golfer.txt'

# print(w_file_name)
w_file = open(f'../athletes/golf/{w_file_name}', 'w+')
w_file.write(f'{title} \n')

# print(f'{title}')
pat0 = '='*len(title)
w_file.write(f'{pat0} \n\n')

tables = soup.find_all('table',  {'class': 'wikitable'})
# print(len(table)) # prints len of table

roster_table = tables[0]
# print(roster_table) # prints roster of the current player
trs = roster_table.find_all('tr')
#print(trs[0])
headers = []
total_player = 0
ths = trs[0].find_all('th')
for th in ths:
    headers.append(th.string.rstrip())

print(headers)
theader = ''
for i in range(len(headers)):
    if i == len(headers)-1:
        theader += headers[len(headers)-1]
    else:
        theader += (headers[i] + ' '*len(headers[i]) + '|' + ' '*len(headers[i]))

# print(theader)

w_file.write(f'{theader}\n')
pat1 = ' '*len(theader)
w_file.write(f'{pat1}\n')


for i in range(1, len(trs)):
    name=editions=''
    tds = trs[i].find_all('td')
    if tds[0].string:
        name = tds[0].string.rstrip()
    if tds[1].a.string:
        a_links = tds[1].find_all('a')
        # print(a_links)
        for a in a_links:
            editions += (a.string.rstrip() + ' ')

    w_file.write(f'{name} | {editions} \n')
    total_player += 1


w_file.write(f'\n\nTotal player: {total_player}\n\n')
w_file.close()

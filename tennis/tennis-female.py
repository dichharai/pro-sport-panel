#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

website_content = requests.get('https://en.wikipedia.org/wiki/List_of_female_tennis_players').text
# print(website_content)

soup = BeautifulSoup(website_content, 'lxml')
# print(soup.prettify())
title = soup.title.string.rstrip()
# writing to a file
write_file_name_list = title.split(' ')
#  print(write_file_name_list)

w_file_name = 'female-tennis-player.txt'

# print(w_file_name)
w_file = open(f'../athletes/tennis/{w_file_name}', 'w+')
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

#print(headers)
theader = ''
for i in range(len(headers)):
    if i == len(headers)-1:
        theader += headers[len(headers)-1]
    elif i != 4:
        theader += (headers[i] + ' '*len(headers[i]) + '|' + ' '*len(headers[i]))
    else:
        continue

#print(theader)

w_file.write(f'{theader}\n')
pat1 = ' '*len(theader)
w_file.write(f'{pat1}\n')

for i in range(1, len(trs)):
    name=birth=death=nationality=awards=''
    tds = trs[i].find_all('td')
    # print(len(tds))
    if tds[0].string:
        name  = tds[0].a.string.rstrip()
    if tds[1].string:
        birth = tds[1].string.rstrip()
    if tds[2].string:
        death = tds[2].string.rstrip()
    if tds[3].find('a'):
        nationality = tds[3].a['title'].rstrip()
    if tds[5].string:
        awards = tds[5].string.rstrip()
    # print(f'{no} | {pos} | {name} | {nationality}')
    w_file.write(f'{name} | {birth} | {death} | {nationality} | {awards}\n')
    total_player += 1


w_file.write(f'\n\nTotal player: {total_player}')
w_file.close()

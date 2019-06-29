#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

file = open('mls-list.txt', 'r')
lines = file.readlines()
link = lines[16].rstrip()
file.close()


website_content = requests.get('https://en.wikipedia.org'+link).text
# print(website_content)

soup = BeautifulSoup(website_content, 'lxml')
# print(soup.prettify())
title = soup.title.string.rstrip()
# writing to a file
write_file_name_list = title.split(' ')
#  print(write_file_name_list)

w_file_name = f'{write_file_name_list[0].lower()}-{write_file_name_list[1].lower()}.txt'

# print(w_file_name)
w_file = open(f'../athletes/soccer/{w_file_name}', 'w+')
w_file.write(f'{title} \n')

# print(f'{title}')
pat0 = '='*len(title)
w_file.write(f'{pat0} \n\n')



tables = soup.find_all('table',  {'class': 'wikitable'})
# print(len(table)) # prints len of table

roster_table = tables[1]
#print(roster_table) # prints roster of the current player
trs = roster_table.find_all('tr')
# print(len(trs))
#print(trs[0])
headers = []
total_player = 0
ths = trs[0].find_all('th')
#print(ths)
for th in ths:
    headers.append(th.string.rstrip())

#print(headers)
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
    tds = trs[i].find_all('td')
    # print(len(tds))
    # print(tds)
    if len(tds):
        no = tds[0].string.rstrip()
        pos = tds[1].a.string.rstrip()
        if tds[2].find('a'):
            name = tds[2].a.string.rstrip()
        else:
            name = tds[2].span.string.rstrip()
        nationality = tds[3].a.string.rstrip()
        # print(f'{no} | {pos} | {name} | {nationality}')
        w_file.write(f'{no} | {pos} | {name} | {nationality}\n')
        total_player += 1


w_file.write(f'\n\nTotal player: {total_player}')

w_file.close()





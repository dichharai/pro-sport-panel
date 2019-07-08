#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

website_content = requests.get('https://en.wikipedia.org/wiki/List_of_American_Championship_Car_winners').text
# print(website_content)

soup = BeautifulSoup(website_content, 'lxml')
# print(soup.prettify())
title = soup.title.string.rstrip()
# writing to a file
write_file_name_list = title.split(' ')
#  print(write_file_name_list)

w_file_name = 'american-championship-car-winners.txt'

# print(w_file_name)
w_file = open(f'../athletes/motor-sports/{w_file_name}', 'w+')
w_file.write(f'{title} \n')

# print(f'{title}')
pat0 = '='*len(title)
w_file.write(f'{pat0} \n\n')

championship = 'National Championships chart'
w_file.write(f'{championship} \n')
pat = '='*len(championship)
w_file.write(f'{pat} \n')

headers = ['Driver', 'Nation', 'AAA (1905) (1916) (1920-1955)', 'USAC (1956-1979)', 'CART (1979-2003)', 'Champ Car World Series (2004-2007)', 'IRL IndyCar Series (1996-present)', 'Combined Total']

space = ' '*5
title = ''
for i in range(len(headers)):
    if i != len(headers)-1:
        title += (headers[i] + space + '|' + space)
    else:
        title += headers[i]

w_file.write(f'{title} \n')

tables = soup.find_all('table', {'class': 'wikitable'})
# print(f'{len(tables)}')

roster_table = tables[0]
# print(roster_table)
trs = roster_table.find_all('tr')
total_player = 0
for i in range(1, len(trs)):
    driver=nation=aaa=usac=cart=champ_car=irl=ct=''
    tds = trs[i].find_all('td')
    if tds[0].find('a'):
        name = tds[0].find_all('span', {'class': 'fn'})
        nation = tds[0].a['title'].rstrip()
        driver = name[0].a['title'].rstrip()
    aaa = tds[1].string.rstrip()
    usac = tds[2].string.rstrip()
    cart = tds[3].string.rstrip()
    champ_car = tds[4].string.rstrip()
    irl = tds[5].string.rstrip()
    ct = tds[6].b.string.rstrip()

    w_file.write(f'{driver} | {nation} | {aaa} | {usac} | {cart} | {champ_car} | {irl} | {ct} \n')
    total_player += 1


w_file.write(f'\n\nTotal player: {total_player} \n\n')

championship = 'Race wins chart'
pat = '='*len(championship)

w_file.write(f'{championship} \n')
w_file.write(f'{pat} \n')

headers.insert(3, 'AAA 1946 Big Car')
title = ''
for i in range(len(headers)):
    if i != len(headers)-1:
        title += (headers[i] + space + '|' + space)
    else:
        title += headers[i]

w_file.write(f'{title} \n')


roster_table_1 = tables[1]
trs = roster_table_1.find_all('tr')
#print(f'{roster_table_1}')
total_player = 0

for i in range(1, len(trs)):
    driver=nation=aaa=aaa_bc=usac=cart=ccws=ic=ct=''
    tds = trs[i].find_all('td')
    name = tds[0].find_all('span', {'class': 'fn'})
    driver = name[0].a['title'].rstrip()
    nation = tds[1].a['title'].rstrip()
    aaa = tds[2].string.rstrip()
    aaa_bc = tds[3].string.rstrip()
    usac = tds[4].string.rstrip()
    cart = tds[5].string.rstrip()
    ccws = tds[6].string.rstrip()
    ic = tds[7].string.rstrip()
    ct = tds[8].b.string.rstrip()

    w_file.write(f'{driver} | {nation} | {aaa} | {aaa_bc} | {usac} | {cart} | {ccws} | {ic} | {ct} \n')
    total_player += 1

w_file.write(f'\n\nTotal player: {total_player} \n\n')

championship = 'Race wins by nationality'
pat = '='*len(championship)

w_file.write(f'{championship}\n')
w_file.write(f'{pat}\n')

# print(tables[8])

headers = ['Rank', 'Country', 'Wins', 'Driver(s)', 'Last Win (Year)']
title = ''
for i in range(len(headers)):
    if i != len(headers)-1:
        title += (headers[i] + space + '|' + space)
    else:
        title += headers[i]

w_file.write(f'{title} \n')

roster_table = tables[8]
trs = roster_table.find_all('tr')

for i in range(1, len(trs)):
    rank=prev_rant=country=wins=driver=last_win=''

    tds = trs[i].find_all('td')
    if tds[0].string:
        rank = tds[0].string.rstrip()
        country = tds[1].a['title'].rstrip()
        wins = tds[2].string.rstrip()
        driver = tds[3].string.rstrip()
        last_win = tds[4].string.rstrip()
        prev_rank = rank
    else:
        rank = prev_rank
        country = tds[0].a['title'].rstrip()
        wins = tds[1].string.rstrip()
        driver = tds[2].string.rstrip()
        last_win = tds[3].string.rstrip()

    w_file.write(f'{rank} | {country} | {wins} | {driver} | {last_win}\n')




w_file.close()
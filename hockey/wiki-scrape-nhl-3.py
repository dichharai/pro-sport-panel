#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

file = open('nhl-links.txt', 'r')
lines = file.readlines()
# print(lines[3])
link1 = lines[5].strip()
file.close()


'''
link = 'https://en.wikipedia.org'+link1
print(link)
'''

website_content = requests.get('https://en.wikipedia.org'+link1).text

total_tenderer = 0
total_skater = 0

soup = BeautifulSoup(website_content, 'lxml')
# print(soup.prettify())
title = soup.title.string.rstrip()


# writing to a file
write_file_name_list = title.split(' ')
# print(write_file_name_list)

w_file_name = f'{write_file_name_list[2].lower()}-{write_file_name_list[3].lower()}-{write_file_name_list[4].lower()}.txt'

# print(w_file_name)
w_file = open(f'../athletes/hockey/{w_file_name}', 'w+')
w_file.write(title + '\n')
# print(f'{title}')
pattern = '='*len(title)
# print(f'{pattern}\n')
w_file.write(pattern + '\n')

total_player = 0

trs = soup.find_all('tr')
# print(f'{len(trs)}') #
# for header
header = []
tr0 = trs[0]
# print(f'{tr0}') # prints tr0  content
tr0_tds = tr0.find_all('th')
header.append(tr0_tds[0].text.rstrip())
header.append('Nationality')
header.append(tr0_tds[7].text.rstrip())
# print(header)
pat0 = ' '*3
header_title = f'{header[0]}{pat0}|{pat0}{header[1]}{pat0}|{pat0}{header[2]}'

# print(f'{header_title}')

w_file.write(f'{header_title}\n')

for i in range(1, len(trs)-15):
    tds = trs[i].find_all('td')
    name = country = year = ''
    if len(tds) >=  2:
        name = tds[0].a.string
        country = tds[1].a['title']
        total_player += 1
    if len(tds) >= 7:
        year = tds[7].string

    # print(f'{name}|{country}|{year}')
    w_file.write(f'{name} | {country} | {year}\n')

#print(f'\n\nTotal  Player: {total_player}')
w_file.write(f'\n\nTotal  Player: {total_player}')
w_file.close()







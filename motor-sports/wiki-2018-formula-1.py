#!/usr/bin/env python3

import requests
import re
from bs4 import BeautifulSoup

website_content = requests.get('https://en.wikipedia.org/wiki/2018_Formula_One_World_Championship').text
# print(website_content)

soup = BeautifulSoup(website_content, 'lxml')
# print(soup.prettify())
title = soup.title.string.rstrip()
# writing to a file
write_file_name_list = title.split(' ')
#  print(write_file_name_list)

w_file_name = '2018-formula-1.txt'

# print(w_file_name)
w_file = open(f'../athletes/motor-sports/{w_file_name}', 'w+')
w_file.write(f'{title} \n')

# print(f'{title}')
pat0 = '='*len(title)
w_file.write(f'{pat0} \n\n')

tables = soup.find_all('table',  {'class': 'wikitable'})
championship = 'Entries'
pat = '='*len(championship)
w_file.write(f'{championship} \n')
w_file.write(f'{pat} \n')

headers = ['Entrant (country, entrant)', 'Constructor', 'Chassels', 'Power unit', 'Race drivers (No., Driver name, Rounds)', 'Free Practice drivers (No, Driver name)']
space = ' '*7
title = ''
for i in range(len(headers)):
    if i != len(headers)-1:
        title += (headers[i] + space + '|' + space)
    else:
        title += headers[i]

w_file.write(f'{title} \n')


roster_table = tables[0]
# print(f'{roster_table}')
trs = roster_table.find_all('tr')

'''
tds = trs[2].find_all('td')
entrant = tds[0].a['title']
cons = tds[1].a.string.rstrip()
entrant += (' ' + tds[1].a['title'].rstrip())
chassis = tds[2].a.string.rstrip()
pu = tds[3].string.rstrip()
no = str(tds[4])
mid_id = no.index(">")
sliced = no[mid_id+1:]
nums = [s for s in re.findall(r'\d+', sliced)]
d_countries = tds[5].find_all('span')
countries = [d_countries[0].a['title'].rstrip(),d_countries[1].a['title']]
d_names = tds[5].find_all('a')
names = [d_names[1].string.rstrip(), d_names[3].string.rstrip()]
round_raw = str(tds[6])
rounds = [round_raw[round_raw.index('>')+1: round_raw.index('<br/>')], round_raw[round_raw.index('<br/>')+5: round_raw.index('</td>')].rstrip()]
fpd = tds[7]
if fpd.find('span'):
    no1 = fpd.span.a['title']
    dn1 = fpd.a.string.rstrip()
else:
    no1 = dn1 = fpd.string


print(f'{no1}{dn1}')
'''


for i in range(2, len(trs)-1):
    entrant=cons=chassis=pu=no=name=rounds=country=no1=dn1=''
    tds = trs[i].find_all('td')
    entrant = (tds[0].a['title'],  tds[1].a['title'].rstrip())
    cons = tds[1].a.string.rstrip()
    chassis = tds[2].a.string.rstrip()
    if tds[3].string:
        pu = tds[3].string.rstrip()
    else:
        pu = 'TAG Heuer'
    no = str(tds[4])
    mid_id = no.index(">")
    sliced = no[mid_id + 1:]
    nums = [s for s in re.findall(r'\d+', sliced)]
    d_countries = tds[5].find_all('span')
    countries = [d_countries[0].a['title'].rstrip(), d_countries[1].a['title']]
    d_names = tds[5].find_all('a')
    names = [d_names[1].string.rstrip(), d_names[3].string.rstrip()]
    round_raw = str(tds[6])
    rounds = [round_raw[round_raw.index('>') + 1: round_raw.index('<br/>')],
              round_raw[round_raw.index('<br/>') + 5: round_raw.index('</td>')].rstrip()]
    if len(tds) == 8:
        fpd = tds[7]
        no1 = country = dn1 = fpd.string.rstrip()
    else:
        no1 = tds[7].string.rstrip()
        fpd = tds[8].find_all('a')
        country = fpd[0]['title'].rstrip()
        dn1 = fpd[1]['title'].rstrip()


    w_file.write(f'{entrant} |  {cons} |  {chassis} | {pu} |  ({nums[0]}, {names[0]},  {rounds[0]}), ({nums[1]}, {names[1]}, {rounds[1]}) | ({no1}, {country}, {dn1}) \n')

w_file.close()
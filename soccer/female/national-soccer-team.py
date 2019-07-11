#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

website_content = requests.get('https://en.wikipedia.org/wiki/United_States_women%27s_national_soccer_team').text
soup = BeautifulSoup(website_content, 'lxml')

title = soup.title.string.rstrip()
pat = '-'*len(title)
print(title)
print(pat)

tables = soup.find_all('table', {'class': 'sortable wikitable plainrowheaders'})

# print(len(tables))
# print(tables[0])
soc_table = tables[0]
trs = soc_table.find_all('tr')
ths = trs[0].find_all('th')

space = ' '*3
header = ''

# print(len(ths))
player_count = 0

for i in range(len(ths)):
    if i != len(ths)-1:
        if ths[i].find('abbr'):
            header += (ths[i].abbr.string.rstrip() + space + '|' + space)
        else:
            header += (ths[i].string.rstrip() + space + '|' + space)

    else:
        header += (ths[i].string.rstrip())

print(header)

player_count = 0

for i in range(1, len(trs)):
    no=pos=player=dob=caps=goals=nation=club=''
    tds = trs[i].find_all('td')
    if len(tds) > 1:

        no = tds[0].string.rstrip()
        pos = tds[1].a.string.rstrip()

        player = trs[i].find('th').a['title'].rstrip()
        dob_span = tds[2].find_all('span')

        dob = dob_span[1].string.rstrip()
        caps = tds[3].string.rstrip()
        goals = tds[4].string.rstrip()
        a_s = tds[5].find_all('a')
        #  print(a_s)
        nation = a_s[0]['title']
        club = a_s[1]['title']

        print(f'{no} | {pos} | {player} | {dob} | {caps} | {goals} | {nation}, {club}')

        player_count += 1

print(f'\n\nTotal  Player: {player_count}')
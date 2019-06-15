#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

website_content = requests.get('https://en.wikipedia.org/wiki/List_of_current_NFC_team_rosters').text

soup = BeautifulSoup(website_content, 'lxml')
# print(soup.prettify())
title = soup.title.string.rstrip()
print(f'{title}')
pat0 = '='*len(title)
print(f'{pat0} \n')

total_players = 0

tables = soup.find_all('table', {'class': 'toccolours'})
#print(len(tables))

# first_table = tables[0]
for table in tables:
    trs = table.find_all('tr')

    # name  of the club
    tr0=trs[0]
    tr0_text = tr0.div.text
    name_list = tr0_text.split('roster')
    club_name = name_list[0] + 'roster'
    print(f'{club_name}')
    pat1 = '='*len(club_name)
    print(f'{pat1}')

    # name of the players
    player_content = trs[1]
    tds = player_content.find_all('td')
    for i in range(len(tds)):
        first_col = tds[i]
        # print(first_col) # prints first col
        for tag in first_col:
            # print(f'{tag.name}') # prints tag_name

            if tag.name == 'b':
                print(f'\n{tag.text.rstrip()}') # for position
                pat2 = '-'*len(tag.text)
                print(f'{pat2}')
            elif tag.name == 'ul':
                lis = tag.find_all('li')
                for li in lis:
                    if li.find('span') and li.find('a'):
                        print(f'{li.span.string}  {li.a.string}')
                        total_players += 1
                    elif li.find('span'):
                        print(f'{li.span.string}')
                        total_players += 1
                    elif li.find('a'):
                        print(f'{li.a.string}')
                        total_players += 1
                    elif li.find('i'):
                        print(f'{li.i.string}\n')
                    else:
                        continue
            elif tag.name == 'p':
                if tag.find('b'):
                    print(f'\n{tag.b.text}')
                    pat3 = '-'*(len(tag.b.text))
                    print(f'{pat3}')


print(f'\nTotal Players: {total_players}')
'''
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
'''

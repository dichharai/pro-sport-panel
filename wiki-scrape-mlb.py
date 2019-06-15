#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

website_content = requests.get('https://en.wikipedia.org/wiki/List_of_Major_League_Baseball_team_rosters').text

soup = BeautifulSoup(website_content, 'lxml')
# print(soup.prettify())
title = soup.title.string
print(f'{title}\n')

tables = soup.find_all('table', {'class': 'toccolours'})
# print(len(tables))
table = tables[0]
# print(table) # prints first table
player_count = 0
for table in tables:
    trs = table.find_all('tr')
    # print(len(trs)) # find length of trs
    name_tr = trs[0] # tr containing name of the roster
    name = name_tr.find('th').div.text # extract name of the roster
    print(f'\n{name}') # prints name of the roster

    header_th = trs[1].find_all('th')
    headers = []
    for header in header_th:
        headers.append(header.text.rstrip())
    # print(headers) # prints headers

    tds = trs[2].find_all('td') # get all tds
    # print(tds[0])
    print(f'{headers[0]}')
    for tag in tds[0]:
        # print(f'**{tag}**')

        if tag.name == 'p':
            print(f'\n**{tag.b.string}**')
        elif tag.name == 'ul':
            # print(type(tag))
            lis = tag.find_all('li')
            for li in lis:
                if li.find('span') and li.find('a'):
                    print(f'{li.span.string} {li.a.string}')
                    player_count += 1
        else:
            continue


    # print(len(tds))

    for tag in tds[2]:
        # print(f'**{tag}**')

        if tag.name == 'p' and tag.find('b'):
            print(f'**{tag.b.string}**')
        elif tag.name == 'ul':
            # print(type(tag))
            lis = tag.find_all('li')
            for li in lis:
                if li.find('span') and li.find('a'):
                    print(f'{li.span.string} {li.a.string}')
                    player_count += 1
        else:
            continue

    print(f'\n{headers[1]}')
    for tag in tds[4]:
        # print(f'**{tag}**')

        if tag.name == 'p' and tag.find('b'):
            print(f'\n**{tag.b.string}**')
        elif tag.name == 'ul':
            # print(type(tag))
            lis = tag.find_all('li')
            for li in lis:
                if li.find('span') and li.find('a'):
                    print(f'{li.span.string} {li.a.string}')
                    player_count += 1
        else:
            continue

    print(f'\n{headers[2]}')
    for tag in tds[6]:
        # print(f'**{tag}**')

        if tag.name == 'p' and tag.find('b'):
            print(f'\n**{tag.b.string}**')
        elif tag.name == 'ul':
            # print(type(tag))
            lis = tag.find_all('li')
            for li in lis:
                if li.find('span') and li.find('a'):
                    print(f'{li.span.string } {li.a.string}')
                    player_count += 1
        else:
            continue

print(f'\n Total Players: {player_count}')

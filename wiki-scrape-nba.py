#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

website_content = requests.get('https://en.wikipedia.org/wiki/List_of_current_NBA_team_rosters').text

soup = BeautifulSoup(website_content, 'lxml')
# print(soup.prettify())
title = soup.title.string
print(f'{title.rstrip()}')
pattern = '='*len(title)
print(f'{pattern}')

tables = soup.find_all('table', {'class': 'toccolours'})
#print(len(tables))
table = tables[0] # print first table
total_player = 0
total_coach = 0
total_ac = 0

for table in tables:
    # print(f'{table}')
    trs = table.find_all('tr')
    team_name = trs[0].text

    print(team_name.rstrip())
    pat2 = '='*len(team_name)
    print(f'{pat2}')

    headers = []
    header_th = trs[1].find_all('th')
    for header in header_th:
        headers.append(header.text.rstrip())
    # print(headers) #prints headers

    data_tr = trs[2]
    # print(data_tr) # tr with data

    table_body = data_tr.find('table').find('tbody')
    # print(table_body) # prints table body
    trs = table_body.find_all('tr')
    # print(trs) prints trs
    for i in range(1, len(trs)):
        tr = trs[i] # first tr
        # print(tr) # prints tds in tr

        tds = tr.find_all('td')

        if tds[1].find('span') and tds[2].find('a'):
            print(f'{tds[1].span.string} {tds[2].a.string}')
        elif tds[1].find('span'):
            print(f'{tds[1].span.string}')
        elif tds[2].find('a'):
            print(f'{tds[2].a.string}')
        else:
            continue

        total_player += 1


    # for finding coaches and assistant coaches
    tds = data_tr.find_all('td')
    # print(tds[len(tds)-1])
    coach_td = tds[len(tds)-1]
    c_headers = coach_td.find_all('dl')
    coach_headers = []
    for header in c_headers:
        coach_headers.append(header.dt.string)


    coach_uls = coach_td.find_all('ul')
    #print(coach_uls)
    head_coach = coach_uls[0].li.a.string
    print(f'\n{coach_headers[0]}')
    pat3 = '-'*len(coach_headers[0])
    print(f'{pat3}')

    print(head_coach)
    total_coach += 1

    if coach_headers[1] == 'Assistant coach(es)':
        print(f'\n{coach_headers[1]}')
        pat4 = '-'*len(coach_headers[1])
        print(f'{pat4}')
        ass_coaches = coach_uls[1].find_all('li')
        for li in ass_coaches:
            if(li.find('a')):
                print(li.a.string)
            else:
                print(li.text)

            total_ac += 1
        # print(coach_headers)

print(f'\n\nTotal Player: {total_player}')
print(f'Total Coaches: {total_coach}')
print(f'Total Assistant Coaches: {total_ac}')


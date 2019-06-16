#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

file = open('nhl-links.txt', 'r')
lines = file.readlines()
# print(lines[3])
link1 = lines[12].strip()
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
write_file_name_list =  title.split(' ')
# print(write_file_name_list)

w_file_name = f'{write_file_name_list[2].lower()}-{write_file_name_list[3].lower()}-{write_file_name_list[4].lower()}.txt'

# print(w_file_name)
w_file = open(f'../athletes/hockey/{w_file_name}', 'w+')
w_file.write(title + '\n')
# print(f'{title}')
pattern = '='*len(title)
# print(f'{pattern}\n')
w_file.write(pattern + '\n')



# for finding headers
position_span = soup.find_all('span', {'class': 'mw-headline'})
positions = []
positions.append(position_span[1].string)
positions.append(position_span[2].string)

# print(positions) # prints  positions



#print(positions)
# for Goaltenders players
pattern0 = '_'*len(positions[0])
# print(f'{positions[0].rstrip()}')
# print(f'{pattern0}\n')

w_file.write(positions[0].rstrip()+'\n')
w_file.write(pattern0 + '\n')


tables = soup.find_all('table', {'class': 'wikitable'})
#print(len(tables))
# for Goaltenders
table_goaltenders = tables[3]
#print(table_goaltenders)
#  print(tables) # prints the table
trs = table_goaltenders.find_all('tr')
#print(trs) # prints all the trs
#print(len(trs))

ths = trs[0].find_all('th')

headers = []

headers.append(ths[0].text.rstrip())
headers.append(ths[1].text.rstrip())
headers.append(ths[2].text.rstrip())

# print(headers)  # prints headers


pattern1 = ' '*5
# print(f'{headers[0]}{pattern1}|{pattern1}{headers[1]}{pattern1}|{pattern1}{headers[2]}')

head1 = f'{headers[0]}{pattern1}|{pattern1}{headers[1]}{pattern1}|{pattern1}{headers[2]}'

# print(head1) #


w_file.write(head1 + '\n')


for i in range(2, len(trs)):
    # print('****')
    # print(tr)

    tds = trs[i].find_all('td')
    # print(len(tds))
    if len(tds)>1:
        name = tds[0].a.string
        nationality = tds[1].a["title"]
        seasons = tds[2].text
        #  print(f'{name} | {nationality} | {num}  | {seasons}')
        data = f'{name} | {nationality} | {seasons}'
        w_file.write(data + '\n')
        total_tenderer += 1


# for Skaters players
pattern2 = '_'*len(positions[1])
# print(f'\n\n{positions[1].rstrip()}')
# print(f'{pattern2}\n')
w_file.write('\n\n' + positions[1].rstrip() + '\n')
w_file.write(pattern2 + '\n')

pattern1 = ' '*5
# print(f'{headers[0]}{pattern1}|{pattern1}{headers[1]}{pattern1}|{pattern1}{headers[2]}')
head2 = f'{headers[0]}{pattern1}|{pattern1}{headers[1]}{pattern1}|{pattern1}{headers[2]}'
w_file.write(head2 + '\n')

table_skaters = tables[4]
# print(table_skaters)
trs = table_skaters.find_all('tr')
#print(trs)
for tr in trs:
    tds = tr.find_all('td')
    # print(len(tds))
    if len(tds) > 1:
        name = tds[0].a.string
        nationality = tds[1].a["title"]
        seasons = tds[3].text
        # print(f'{name} | {nationality} | {seasons}')
        data = f'{name} | {nationality} | {seasons}'
        w_file.write(data + '\n')
        total_skater += 1

# print(f'\n\nTotal Goaltenders: {total_tenderer}')
# print(f'Total Skaters: {total_skater}')

tg = f'\n\nTotal Goaltenders: {total_tenderer}'
ts = f'Total Skaters: {total_skater}'

w_file.write(tg + '\n')
w_file.write(ts + '\n')

w_file.close()


















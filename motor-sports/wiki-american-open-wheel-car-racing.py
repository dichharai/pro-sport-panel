#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

website_content = requests.get('https://en.wikipedia.org/wiki/American_open-wheel_car_racing').text
# print(website_content)

soup = BeautifulSoup(website_content, 'lxml')
# print(soup.prettify())
title = soup.title.string.rstrip()
# writing to a file
write_file_name_list = title.split(' ')
#  print(write_file_name_list)

w_file_name = 'usa-open-wheel-car-racing.txt'

# print(w_file_name)
w_file = open(f'../athletes/motor-sports/{w_file_name}', 'w+')
w_file.write(f'{title} \n')

# print(f'{title}')
pat0 = '='*len(title)
w_file.write(f'{pat0} \n')

tables = soup.find_all('table',  {'class': 'wikitable'})
# print(f'{len(tables)}')

headers = ['Year', 'Champion']
space = ' '*5
title = ''
for i in range(len(headers)):
    if i != (len(headers)-1):
        title += (headers[i] + space + '|' + space)
    else:
        title += headers[i]

w_file.write(f'{title}\n')

trs = tables[0].find_all('tr')

championship = 'AAA National Championship'
pat = '-'*len(championship)
w_file.write(f'\n{championship}\n')
w_file.write(f'{pat}\n')

sentinel=0
racer = 0

for i in range(2, len(trs)):
    tr=trs[i]
    if not tr.find('th'):
        tds = tr.find_all('td')
        # print(tds)
        year = nation = name = ''
        if len(tds) == 2:
            year = tds[0].string.rstrip()
            a_s = tds[1].find_all('a')
            nation = a_s[0]['title']
            name = a_s[1]['title']

            w_file.write(f'{year}, ({nation}, {name})\n')
            sentinel += 1
            racer += 1
        else:
            str_para = str(tds[0])
            year = str_para[str_para.find('>') + 1:str_para.find(':')]
            descrip = 'No championships'
            # print(f'{type(tds[0])}')
            w_file.write(f'{year}, {descrip}\n')
            sentinel += 1
    else:
        break

print(f'Total Racer: {racer}')


championship = 'USAC National Championship'
pat = '-'*len(championship)
w_file.write(f'\n{championship}\n')
w_file.write(f'{pat}\n')
sentinel += 2
racer = 0

for i in range(sentinel+1, len(trs)):
    tr = trs[i]
    tds = tr.find_all('td')
    if not tr.find('th')  and len(tds) == 2 or  len(tds) ==1:

        # print(tds)
        year = nation = name = ''
        if len(tds) == 2:
            year = tds[0].string.rstrip()
            a_s = tds[1].find_all('a')
            nation = a_s[0]['title']
            name = a_s[1]['title']

            w_file.write(f'{year}, ({nation}, {name})\n')
            sentinel += 1
            racer += 1
        else:
            str_para = str(tds[0])
            year = str_para[str_para.find('>') + 1:str_para.find(':')]
            descrip = 'No championships'
            # print(f'{type(tds[0])}')
            w_file.write(f'{year}, {descrip}\n')
            sentinel += 1
            racer += 1
    else:
        break

print(f'Total Racer: {racer}')

championship = 'USAC Gold  Crown Championship'
pat = '-'*len(championship)
w_file.write(f'\n{championship}\n')
w_file.write(f'{pat}\n')
cart_start = sentinel
sentinel += 5
racer = 0

for i in range(sentinel, len(trs)):
    tr = trs[i]
    # print(tr)
    tds = tr.find_all('td')
    # print(tds)
    # print(tds[0])
    if not tr.find('th'):

        year = tds[0].a.string.rstrip()
        a_s = tds[1].find_all('a')
        nation = a_s[0]['title']
        name = a_s[1]['title']

        w_file.write(f'{year}, ({nation}, {name})\n')

        sentinel += 1
        racer += 1
    else:
        break

print(f'Total Racer: {racer}')

championship = 'Indy Racing League'
pat = '-'*len(championship)
w_file.write(f'\n{championship}\n')
w_file.write(f'{pat}\n')
sentinel += 1
racer = 0

for i in range(sentinel, len(trs)):
    tr = trs[i]
    # print(tr)
    tds = tr.find_all('td')
    # print(tds)
    # print(tds[0])
    if not tr.find('th'):

        year = tds[0].a.string.rstrip()
        a_s = tds[1].find_all('a')
        nation = a_s[0]['title']
        name = a_s[1]['title']

        w_file.write(f'{year}, ({nation}, {name})\n')

        sentinel += 1
        racer += 1

    else:
        break

print(f'Total Racer: {racer}')
championship = 'IndyCar Series'
pat = '-'*len(championship)
w_file.write(f'\n{championship}\n')
w_file.write(f'{pat}\n')
sentinel += 1
racer = 0

for i in range(sentinel, len(trs)):
    tr = trs[i]
    # print(tr)
    tds = tr.find_all('td')
    # print(tds)
    # print(tds[0])
    if not tr.find('th'):
        year = tds[0].a.string.rstrip()
        a_s = tds[1].find_all('a')
        nation = a_s[0]['title']
        name = a_s[1]['title']

        w_file.write(f'{year}, ({nation}, {name})\n')

        sentinel += 1
        racer += 1

    elif tr.find('th') and len(tds)==2:
        year = tds[0].a.string.rstrip()
        a_s = tds[1].find_all('a')
        nation = a_s[0]['title']
        name = a_s[1]['title']

        w_file.write(f'{year}, ({nation}, {name})\n')

        sentinel += 1
        racer += 1
    else:
        break

print(f'Total Racer: {racer}')

championship = 'IndyCar Series'
pat = '-'*len(championship)
w_file.write(f'\n{championship}\n')
w_file.write(f'{pat}\n')
sentinel += 1
racer = 0

for i in range(sentinel, len(trs)):
    tr = trs[i]
    # print(tr)
    tds = tr.find_all('td')
    # print(tds)
    # print(tds[0])
    if not tr.find('th'):

        year = tds[0].a.string.rstrip()
        a_s = tds[1].find_all('a')
        nation = a_s[0]['title']
        name = a_s[1]['title']

        w_file.write(f'{year}, ({nation}, {name})\n')

        sentinel += 1
        racer += 1
    else:
        break

print(f'Total Racer: {racer}')
ccws = sentinel+2

championship = 'CART Indy Car Series'
pat = '-'*len(championship)
w_file.write(f'\n{championship}\n')
w_file.write(f'{pat}\n')
# print(trs[cart_start+2])
racer = 0
for i in range(cart_start+2, len(trs)):
    tr  = trs[i]
    tds = tr.find_all('td')

    header = ''
    if tr.find('th'):
        ths = tr.find_all('th')
        if len(ths) > 1:
            str_header = str(ths[1])
            if '<sup' in str_header:
                header = str_header[str_header.index('th>') + 3:str_header.index('<sup')]
            else:
                header = str_header[str_header.index('th>') + 3:str_header.index('</th>')].rstrip()


        else:
            header = tr.th.string.rstrip()

    if header == 'Champ Car World Series':
        break

    # print(tds)
    if len(tds) == 4:
        year = tds[2].a.string.rstrip()
        a_s = tds[3].find_all('a')
        nation = a_s[0]['title']
        name = a_s[1]['title']

        w_file.write(f'{year}, ({nation}, {name})\n')

        sentinel += 1
        racer += 1

    elif len(tds) == 3:
        year = tds[1].a.string.rstrip()
        a_s = tds[2].find_all('a')
        nation = a_s[0]['title']
        name = a_s[1]['title']

        w_file.write(f'{year}, ({nation}, {name})\n')

        sentinel += 1
        racer += 1

print(f'Total Racer: {racer}')
championship = 'Champ Car World Series'
pat = '-'*len(championship)
w_file.write(f'\n{championship}\n')
w_file.write(f'{pat}\n')

'''
#print(trs[ccws])
for i in range(ccws, len(trs)):
    tr = trs[i]

    if not tr.find('th'):
        tds = tr.find_all('td')
        year = tds[2].a.string.rstrip()
        a_s = tds[3].find_all('a')
        nation = a_s[0]['title']
        name = a_s[1]['title']

        w_file.write(f'{year}, ({nation}, {name})\n')

        sentinel += 1
    else:
        break
'''








'''

for i in range(1, len(trs)):
    tr = trs[i]

    if tr.find('th'):
        ths = tr.find_all('th')
        if len(ths)>1:
            str_header=str(ths[1])
            if '<sup' in str_header:
                header = str_header[str_header.index('th>')+3:str_header.index('<sup')]
            else:
                header = str_header[str_header.index('th>')+3:str_header.index('</th>')].rstrip()


        else:
            header = tr.th.string.rstrip()



        w_file.write(f'\n{header}\n')
        pat = '-'*len(header)
        w_file.write(f'{pat}\n')

    elif header == 'CART Indy Car Series':
        year=nation=name=''
        tds = tr.find_all('td')

        year = tds[2].a.string.rstrip()
        a_s = tds[1].find_all('a')
        nation = a_s[0]['title']
        name = a_s[1]['title']

        w_file.write(f'{year}, ({nation}, {name})\n')



    else:
        tds = tr.find_all('td')
        year=nation=name=''
        if len(tds) == 2:
            year = tds[0].string.rstrip()
            a_s = tds[1].find_all('a')
            nation=a_s[0]['title']
            name=a_s[1]['title']

            w_file.write(f'{year}, ({nation}, {name})\n')
        else:
            str_para = str(tds[0])
            year = str_para[str_para.find('>')+1:str_para.find(':')]
            descrip = 'No championships'
            # print(f'{type(tds[0])}')
            w_file.write(f'{year}, {descrip}\n')

'''




w_file.close()
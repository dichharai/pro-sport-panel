#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

website_content = requests.get('https://en.wikipedia.org/wiki/List_of_WWE_personnel').text

soup = BeautifulSoup(website_content, 'lxml')
# print(soup.prettify())
title = soup.title.string.rstrip()
print(f'{title}')
pat0 = '='*len(title)
print(f'{pat0} \n')

total_players = 0

tables = soup.find_all('table', {'class': 'wikitable'})
# print(f'length of tables {len(tables)}.')

rosters = ['McMahon family','Raw', 'SmackDown', '205 Live', 'NXT', 'NXT UK',  'Unassigned wrestlers', 'Performance Center recruits', 'U.K. Performance Center recruits', 'Refrees', 'Broadcast team', 'Ambassadors','Backstage personnel', 'Creative team', 'Music department', 'Producers', 'WWE Performance Center staff', 'WWE Corporate staff']
table0 = tables[0]

# print(f'{table0}')
print(f'{rosters[0]}')
pat0 = '-'*len(rosters[0])
print(f'{pat0}\n')

trs = table0.find_all('tr')
ths = trs[0].find_all('th')

header = ''
space = ' '*5
for i in range(len(ths)):
    if i != len(ths)-1:
        header += (ths[i].string.rstrip() + space + '|' + space)
    else:
        header += (ths[i].string.rstrip())

print(f'{header}')
owners_count = 0

for i in range(1, len(trs)):
    name=real_name=notes=''

    tds = trs[i].find_all('td')
    name =  tds[0].a.string.rstrip()
    real_name = tds[1].span.string.rstrip()
    a_notes = tds[2].find_all('a')
    if len(a_notes):
        for a in a_notes:
            notes += (a.string + ',  ')

    if tds[2].string:
        notes += tds[2].string.rstrip()

    owners_count += 1

    print(f'{name} | {real_name} | {notes}')

print(f'\nTotal owners: {owners_count}\n')

print(f'{rosters[1]}')
pat0 = '-'*len(rosters[1])
print(f'{pat0}\n')

print(f'Male wrestlers')
pat1 = '-'*len('Male wrestlers')
print(f'{pat1}\n')

print(f'{header}')

trs = tables[1].find_all('tr')
raw_male_player_count = 0

for i in range(1, len(trs)):
    name=real_name=notes=''

    tds = trs[i].find_all('td')
    name = tds[0].a.string.rstrip()
    if tds[1].span:
        real_name = tds[1].span.string.rstrip()
    else:
        real_name = tds[1].string

    note = tds[2].text.rstrip()
    if '[' in note:
        idx = note.find("[")
        # print(f'{note.find("[")}')
        # print(f'idx: {idx}')
        notes += (note[0: int(idx)])
    elif tds[2].a and ('[' not in tds[2].a.string):
        notes += tds[2].a.string
    else:
        notes += note


    raw_male_player_count += 1

    print(f'{name} | {real_name} | {notes}')

print(f'\nTotal owners: {raw_male_player_count}\n')


print(f'Female wrestlers')
pat1 = '-'*len('Female wrestlers')
print(f'{pat1}\n')

trs = tables[2].find_all('tr')
raw_female_player_count = 0

print(f'{header}')

for i in range(1, len(trs)):
    name=real_name=notes=''

    tds = trs[i].find_all('td')
    name =  tds[0].a.string.rstrip()
    if tds[1].span:
        real_name = tds[1].span.string.rstrip()
    else:
        real_name = tds[1].string

    if tds[2].text:
        note = tds[2].text.rstrip()
        if '[' in note:
            idx = note.find("[")
            # print(f'{note.find("[")}')
            #print(f'idx: {idx}')
            notes += (note[0: int(idx)])
        elif tds[2].a and ('[' not in tds[2].a.string):
            notes += tds[2].a.string
        else:
            notes += note


    raw_female_player_count += 1

    print(f'{name} | {real_name} | {notes}')

print(f'\nTotal owners: {raw_female_player_count}\n')

print(f'Other on-air personnel')
pat0 = '-'*len('Other on-air  personnel')
print(f'{pat0}')

trs = tables[3].find_all('tr')
raw_on_air_count = 0

print(f'{header}')

for i in range(1, len(trs)):
    name=real_name=notes=''

    tds = trs[i].find_all('td')
    name =  tds[0].a.string.rstrip()
    if tds[1].span:
        real_name = tds[1].span.string.rstrip()
    else:
        real_name = tds[1].string

    note = tds[2].text.rstrip()
    if '[' in note:
        idx = note.find("[")
        # print(f'{note.find("[")}')
        # print(f'idx: {idx}')
        notes += (note[0: int(idx)])
    elif tds[2].a and ('[' not in tds[2].a.string):
        notes += tds[2].a.string
    else:
        notes  += note


    raw_on_air_count += 1

    print(f'{name} | {real_name} | {notes}')

print(f'\nTotal Raw Other on-air personnel: {raw_on_air_count}\n')

print(f'{rosters[2]}')
pat0 = '-'*len(rosters[2])
print(f'{pat0}\n')


print(f'Male wrestlers')
pat1 = '-'*len('Male wrestlers')
print(f'{pat1}')

sd_count = 0
trs = tables[4].find_all('tr')
for i in range(1, len(trs)):
    name=real_name=notes=''

    tds = trs[i].find_all('td')
    name =  tds[0].a.string.rstrip()
    if tds[1].span:
        real_name = tds[1].span.string.rstrip()
    else:
        real_name = tds[1].string

    note = tds[2].text.rstrip()
    if '[' in note:
        idx = note.find("[")
        # print(f'{note.find("[")}')
        # print(f'idx: {idx}')
        notes += (note[0: int(idx)])
    elif tds[2].a and ('[' not in tds[2].a.string):
        notes += tds[2].a.string
    else:
        notes  += note


    sd_count += 1

    print(f'{name} | {real_name} | {notes}')


print(f'\nTotal SmackDown Male: {sd_count}\n')

print(f'Female wrestlers')
pat0 = '-'*len('Female wrestlers')
print(f'{pat0}')

sdf_count = 0
trs = tables[5].find_all('tr')
for i in range(1, len(trs)):
    name=real_name=notes=''

    tds = trs[i].find_all('td')
    name =  tds[0].a.string.rstrip()
    if tds[1].span:
        real_name = tds[1].span.string.rstrip()
    else:
        real_name = tds[1].string

    note = tds[2].text.rstrip()
    if '[' in note:
        idx = note.find("[")
        # print(f'{note.find("[")}')
        # print(f'idx: {idx}')
        notes += (note[0: int(idx)])
    elif tds[2].a and ('[' not in tds[2].a.string):
        notes += tds[2].a.string
    else:
        notes  += note


    sdf_count += 1

    print(f'{name} | {real_name} | {notes}')

print(f'\nTotal SmackDown Female: {sdf_count}\n')

print(f'Other on-air personnel')
pat0 = '-'*len('Other on-air  personnel')
print(f'{pat0}')

trs = tables[6].find_all('tr')
sd_on_air_count = 0

print(f'{header}')

for i in range(1, len(trs)):
    name=real_name=notes=''

    tds = trs[i].find_all('td')
    name =  tds[0].a.string.rstrip()
    if tds[1].span:
        real_name = tds[1].span.string.rstrip()
    else:
        real_name = tds[1].string

    note = tds[2].text.rstrip()
    if '[' in note:
        idx = note.find("[")
        # print(f'{note.find("[")}')
        # print(f'idx: {idx}')
        notes += (note[0: int(idx)])
    elif tds[2].a and ('[' not in tds[2].a.string):
        notes += tds[2].a.string
    else:
        notes  += note


    sd_on_air_count += 1

    print(f'{name} | {real_name} | {notes}')

print(f'\nTotal Smackdown on-air Personnel: {sd_on_air_count}\n')


print(f'{rosters[3]}')
pat0 = '-'*len(rosters[3])
print(f'{pat0}')

print('Male wrestlers')
pat1 = '-'*len('Male wrestlers')
print(f'{pat1}')

live_count = 0
trs = tables[7].find_all('tr')
for i in range(1, len(trs)):
    name=real_name=notes=''

    tds = trs[i].find_all('td')
    name =  tds[0].a.string.rstrip()
    if tds[1].span:
        real_name = tds[1].span.string.rstrip()
    else:
        real_name = tds[1].string

    note = tds[2].text.rstrip()
    if '[' in note:
        idx = note.find("[")
        # print(f'{note.find("[")}')
        # print(f'idx: {idx}')
        notes += (note[0: int(idx)])
    elif tds[2].a and ('[' not in tds[2].a.string):
        notes += tds[2].a.string
    else:
        notes += note


    live_count += 1

    print(f'{name} | {real_name} | {notes}')

print(f'\nTotal Live Male: {live_count}\n')

print(f'Other on-air personnel')
pat0 = '-'*len('Other on-air  personnel')
print(f'{pat0}')

trs = tables[8].find_all('tr')
live_on_air_count = 0

print(f'{header}')

for i in range(1, len(trs)):
    name=real_name=notes=''

    tds = trs[i].find_all('td')
    name =  tds[0].a.string.rstrip()
    if tds[1].span:
        real_name = tds[1].span.string.rstrip()
    else:
        real_name = tds[1].string

    note = tds[2].text.rstrip()
    if '[' in note:
        idx = note.find("[")
        # print(f'{note.find("[")}')
        # print(f'idx: {idx}')
        notes += (note[0: int(idx)])
    elif tds[2].a and ('[' not in tds[2].a.string):
        notes += tds[2].a.string
    else:
        notes  += note


    live_on_air_count += 1

    print(f'{name} | {real_name} | {notes}')

print(f'\nTotal Live on-air Personnel: {live_on_air_count}\n')


print(f'{rosters[4]}')
pat0 = '-'*len(rosters[4])
print(f'{pat0}')

print('Male wrestlers')
pat1 = '-'*len('Male wrestlers')
print(f'{pat1}')

print(f'{header}')
nxt_count = 0
trs = tables[9].find_all('tr')
for i in range(1, len(trs)):
    name=real_name=notes=''

    tds = trs[i].find_all('td')
    name =  tds[0].a.string.rstrip()
    if tds[1].span:
        real_name = tds[1].span.string.rstrip()
    else:
        real_name = tds[1].string

    note = tds[2].text.rstrip()
    if '[' in note:
        idx = note.find("[")
        # print(f'{note.find("[")}')
        # print(f'idx: {idx}')
        notes += (note[0: int(idx)])
    elif tds[2].a and ('[' not in tds[2].a.string):
        notes += tds[2].a.string
    else:
        notes += note


    nxt_count += 1

    print(f'{name} | {real_name} | {notes}')

print(f'\nTotal Nxt Male: {nxt_count}\n')


print('Female wrestlers')
pat1 = '-'*len('Female wrestlers')
print(f'{pat1}')

print(f'{header}')

f_nxt_count = 0
trs = tables[10].find_all('tr')
for i in range(1, len(trs)):
    name=real_name=notes=''

    tds = trs[i].find_all('td')
    name =  tds[0].a.string.rstrip()
    if tds[1].span:
        real_name = tds[1].span.string.rstrip()
    else:
        real_name = tds[1].string

    note = tds[2].text.rstrip()
    if '[' in note:
        idx = note.find("[")
        # print(f'{note.find("[")}')
        # print(f'idx: {idx}')
        notes += (note[0: int(idx)])
    elif tds[2].a and ('[' not in tds[2].a.string):
        notes += tds[2].a.string
    else:
        notes += note


    f_nxt_count += 1

    print(f'{name} | {real_name} | {notes}')

print(f'\nTotal Nxt Female: {f_nxt_count}\n')

print(f'Other on-air personnel')
pat0 = '-'*len('Other on-air  personnel')
print(f'{pat0}')

trs = tables[11].find_all('tr')
nxt_on_air_count = 0

print(f'{header}')

for i in range(1, len(trs)):
    name=real_name=notes=''

    tds = trs[i].find_all('td')
    name =  tds[0].a.string.rstrip()
    if tds[1].span:
        real_name = tds[1].span.string.rstrip()
    else:
        real_name = tds[1].string

    note = tds[2].text.rstrip()
    if '[' in note:
        idx = note.find("[")
        # print(f'{note.find("[")}')
        # print(f'idx: {idx}')
        notes += (note[0: int(idx)])
    elif tds[2].a and ('[' not in tds[2].a.string):
        notes += tds[2].a.string
    else:
        notes  += note


    nxt_on_air_count += 1

    print(f'{name} | {real_name} | {notes}')

print(f'\nTotal Nxt on-air Personnel: {nxt_on_air_count}\n')


print(f'{rosters[5]}')
pat0 = '-'*len(rosters[5])
print(f'{pat0}')

print('Male wrestlers')
pat1 = '-'*len('Male wrestlers')
print(f'{pat1}')

print(f'{header}')
nxt_uk_count = 0
trs = tables[12].find_all('tr')
for i in range(1, len(trs)):
    name=real_name=notes=''

    tds = trs[i].find_all('td')
    name =  tds[0].a.string.rstrip()
    if tds[1].span:
        real_name = tds[1].span.string.rstrip()
    else:
        real_name = tds[1].string

    note = tds[2].text.rstrip()
    if '[' in note:
        idx = note.find("[")
        # print(f'{note.find("[")}')
        # print(f'idx: {idx}')
        notes += (note[0: int(idx)])
    elif tds[2].a and ('[' not in tds[2].a.string):
        notes += tds[2].a.string
    else:
        notes += note


    nxt_uk_count += 1

    print(f'{name} | {real_name} | {notes}')

print(f'\nTotal Nxt UK Male: {nxt_uk_count}\n')

print('Female wrestlers')
pat1 = '-'*len('Female wrestlers')
print(f'{pat1}')

print(f'{header}')

f_nxt_uk_count = 0
trs = tables[13].find_all('tr')
for i in range(1, len(trs)):
    name=real_name=notes=''

    tds = trs[i].find_all('td')
    name =  tds[0].a.string.rstrip()
    if tds[1].span:
        real_name = tds[1].span.string.rstrip()
    else:
        real_name = tds[1].string

    note = tds[2].text.rstrip()
    if '[' in note:
        idx = note.find("[")
        # print(f'{note.find("[")}')
        # print(f'idx: {idx}')
        notes += (note[0: int(idx)])
    elif tds[2].a and ('[' not in tds[2].a.string):
        notes += tds[2].a.string
    else:
        notes += note


    f_nxt_uk_count += 1

    print(f'{name} | {real_name} | {notes}')

print(f'\nTotal Nxt UK Female: {f_nxt_uk_count}\n')

print(f'Other on-air personnel')
pat0 = '-'*len('Other on-air  personnel')
print(f'{pat0}')

trs = tables[14].find_all('tr')
nxt_uk_on_air_count = 0

print(f'{header}')

for i in range(1, len(trs)):
    name=real_name=notes=''

    tds = trs[i].find_all('td')
    name =  tds[0].a.string.rstrip()
    if tds[1].span:
        real_name = tds[1].span.string.rstrip()
    else:
        real_name = tds[1].string

    note = tds[2].text.rstrip()
    if '[' in note:
        idx = note.find("[")
        # print(f'{note.find("[")}')
        # print(f'idx: {idx}')
        notes += (note[0: int(idx)])
    elif tds[2].a and ('[' not in tds[2].a.string):
        notes += tds[2].a.string
    else:
        notes  += note


    nxt_uk_on_air_count += 1

    print(f'{name} | {real_name} | {notes}')

print(f'\nTotal Nxt UK on-air Personnel: {nxt_uk_on_air_count}\n')


print(f'{rosters[6]}')
pat0 = '-'*len(rosters[6])
print(f'{pat0}')

print(f'{header}')
ua_count = 0

trs = tables[15].find_all('tr')
for i in range(1, len(trs)):
    name=real_name=notes=''

    tds = trs[i].find_all('td')
    name =  tds[0].a.string.rstrip()
    if tds[1].span:
        real_name = tds[1].span.string.rstrip()
    else:
        real_name = tds[1].string

    note = tds[2].text.rstrip()
    if '[' in note:
        idx = note.find("[")
        # print(f'{note.find("[")}')
        # print(f'idx: {idx}')
        notes += (note[0: int(idx)])
    elif tds[2].a and ('[' not in tds[2].a.string):
        notes += tds[2].a.string
    else:
        notes  += note


    ua_count += 1

    print(f'{name} | {real_name} | {notes}')

print(f'\nTotal Unassigned wrestlers: {ua_count}\n')

print(f'{rosters[7]}')
pat2 = '-'*len(rosters[7])
print(f'{pat2}')

print(f'U.S. Performance Center recruits')
pat3 = '-'*len('U.S. Performance Center recruits')
print(f'{pat3}')

print('Male wrestlers')
pat1 = '-'*len('Male wrestlers')
print(f'{pat1}')

print(f'{header}')
pc_usm_count = 0
trs = tables[16].find_all('tr')
for i in range(1, len(trs)):
    name=real_name=notes=''

    tds = trs[i].find_all('td')
    if tds[0].a:

        name = tds[0].text
        idx = name.find('[')
        name = name[0: int(idx)]

    else:
        name = tds[0].text.rstrip()

    if tds[1].span:
        real_name = tds[1].span.string.rstrip()
    else:
        real_name = tds[1].string

    note = tds[2].text.rstrip()
    if '[' in note:
        idx = note.find("[")
        # print(f'{note.find("[")}')
        # print(f'idx: {idx}')
        notes += (note[0: int(idx)])
    elif tds[2].a and ('[' not in tds[2].a.string):
        notes += tds[2].a.string
    else:
        notes += note


    pc_usm_count += 1

    print(f'{name} | {real_name} | {notes}')

print(f'\nTotal Performance Center Recruits US Male: {pc_usm_count}\n')

print('Female wrestlers')
pat0  = '-'*len('Female wrestlers')
print(f'{pat0}')

print(f'{header}')
pc_usf_count = 0
trs = tables[17].find_all('tr')
for i in range(1, len(trs)):
    name=real_name=notes=''

    tds = trs[i].find_all('td')
    if tds[0].a:

        name = tds[0].text
        idx = name.find('[')
        name = name[0: int(idx)]

    else:
        name = tds[0].text.rstrip()

    if tds[1].span:
        real_name = tds[1].span.string.rstrip()
    else:
        real_name = tds[1].string

    note = tds[2].text.rstrip()
    if '[' in note:
        idx = note.find("[")
        # print(f'{note.find("[")}')
        # print(f'idx: {idx}')
        notes += (note[0: int(idx)])
    elif tds[2].a and ('[' not in tds[2].a.string):
        notes += tds[2].a.string
    else:
        notes += note


    pc_usf_count += 1

    print(f'{name} | {real_name} | {notes}')

print(f'\nTotal Performance Center Recruits US Female: {pc_usf_count}\n')


print(f'{rosters[8]}')
pat = '-'*len(rosters[8])
print(f'{pat}')

print('Male wrestler')
pat0 = '-'*len('Male  wrestler')
print(f'{pat0}')


print(f'{header}')
pc_uk_count = 0
trs = tables[18].find_all('tr')
for i in range(1, len(trs)):
    name=real_name=notes=''

    tds = trs[i].find_all('td')
    if tds[0].a:

        name = tds[0].text
        idx = name.find('[')
        name = name[0: int(idx)]

    else:
        name = tds[0].text.rstrip()

    if tds[1].span and not tds[1].i:
        real_name = tds[1].span.string.rstrip()
    elif tds[1].i:
        real_name = tds[1].i.string.strip()
    else:
        real_name = tds[1].text.strip()

    note = tds[2].text.rstrip()
    if '[' in note:
        idx = note.find("[")
        # print(f'{note.find("[")}')
        # print(f'idx: {idx}')
        notes += (note[0: int(idx)])
    elif tds[2].a and ('[' not in tds[2].a.string):
        notes += tds[2].a.string
    else:
        notes += note


    pc_uk_count += 1

    print(f'{name} | {real_name} | {notes}')

print(f'\nTotal Performance Center Recruits UK Male: {pc_uk_count}\n')

print(f'{rosters[9]}')
pat = '-'*len(rosters[9])
print(f'{pat}')

print(f'{header}')
refree_count = 0
trs = tables[19].find_all('tr')
for i in range(1, len(trs)):
    name=real_name=notes=''

    tds = trs[i].find_all('td')
    if tds[0].a:

        name = tds[0].text
        idx = name.find('[')
        name = name[0: int(idx)]

    else:
        name = tds[0].text.rstrip()

    if tds[1].span and not tds[1].i:
        real_name = tds[1].span.string.rstrip()
    elif tds[1].i:
        real_name = tds[1].i.string.strip()
    else:
        real_name = tds[1].text.strip()

    note = tds[2].text.rstrip()
    if '[' in note:
        idx = note.find("[")
        # print(f'{note.find("[")}')
        # print(f'idx: {idx}')
        notes += (note[0: int(idx)])
    elif tds[2].a and ('[' not in tds[2].a.string):
        notes += tds[2].a.string
    else:
        notes += note


    refree_count += 1

    print(f'{name} | {real_name} | {notes}')

print(f'\nTotal Refree Count: {refree_count}\n')


print(f'{rosters[10]}')
pat = '-'*len(rosters[10])
print(f'{pat}')

print(f'{header}')
b_count = 0
trs = tables[20].find_all('tr')
for i in range(1, len(trs)):
    name=real_name=notes=''

    tds = trs[i].find_all('td')
    if tds[0].a:

        name = tds[0].text
        idx = name.find('[')
        name = name[0: int(idx)]

    else:
        name = tds[0].text.rstrip()

    if tds[1].span and not tds[1].i:
        real_name = tds[1].span.string.rstrip()
    elif tds[1].i:
        real_name = tds[1].i.string.strip()
    else:
        real_name = tds[1].text.strip()

    note = tds[2].text.rstrip()
    if '[' in note:
        idx = note.find("[")
        # print(f'{note.find("[")}')
        # print(f'idx: {idx}')
        notes += (note[0: int(idx)])
    elif tds[2].a and ('[' not in tds[2].a.string):
        notes += tds[2].a.string
    else:
        notes += note


    b_count += 1

    print(f'{name} | {real_name} | {notes}')

print(f'\nTotal Broadcast team Count: {b_count}\n')

print('Off-screen personnel')
pat = '-'*len('Off-screen personnel')
print(f'{pat}')

print(f'{rosters[11]}')
pat =  '-'*len(rosters[11])
print(f'{pat}')

print(f'{header}')
a_count = 0
trs = tables[21].find_all('tr')
for i in range(1, len(trs)):
    name=real_name=notes=''

    tds = trs[i].find_all('td')
    if tds[0].a:

        name = tds[0].text
        idx = name.find('[')
        name = name[0: int(idx)]

    else:
        name = tds[0].text.rstrip()

    if tds[1].span and not tds[1].i:
        real_name = tds[1].span.string.rstrip()
    elif tds[1].i:
        real_name = tds[1].i.string.strip()
    else:
        real_name = tds[1].text.strip()

    note = tds[2].text.rstrip()
    if '[' in note:
        idx = note.find("[")
        # print(f'{note.find("[")}')
        # print(f'idx: {idx}')
        notes += (note[0: int(idx)])
    elif tds[2].a and ('[' not in tds[2].a.string):
        notes += tds[2].a.string
    else:
        notes += note


    a_count += 1

    print(f'{name} | {real_name} | {notes}')

print(f'\nTotal Ambassadors Count: {a_count}\n')

print(f'{rosters[12]}')
pat =  '-'*len(rosters[12])
print(f'{pat}')

print(f'{header}')
bp_count = 0
trs = tables[22].find_all('tr')
for i in range(1, len(trs)):
    name=real_name=notes=''

    tds = trs[i].find_all('td')
    if tds[0].a:

        name = tds[0].text
        idx = name.find('[')
        name = name[0: int(idx)]

    else:
        name = tds[0].text.rstrip()

    if tds[1].span and not tds[1].i:
        real_name = tds[1].span.string.rstrip()
    elif tds[1].i:
        real_name = tds[1].i.string.strip()
    else:
        real_name = tds[1].text.strip()

    note = tds[2].text.rstrip()
    if '[' in note:
        idx = note.find("[")
        # print(f'{note.find("[")}')
        # print(f'idx: {idx}')
        notes += (note[0: int(idx)])
    elif tds[2].a and ('[' not in tds[2].a.string):
        notes += tds[2].a.string
    else:
        notes += note


    bp_count += 1

    print(f'{name} | {real_name} | {notes}')

print(f'\nTotal Backstage personnel Count: {bp_count}\n')

print(f'{rosters[13]}')
pat = '-'*len(rosters[13])
print(f'{pat}')

print(f'{header}')
ct_count = 0
trs = tables[23].find_all('tr')
for i in range(1, len(trs)):
    name=real_name=notes=''

    tds = trs[i].find_all('td')
    if tds[0].a:

        name = tds[0].text
        idx = name.find('[')
        name = name[0: int(idx)]

    else:
        name = tds[0].text.rstrip()

    if tds[1].span and not tds[1].i:
        real_name = tds[1].span.string.rstrip()
    elif tds[1].i:
        real_name = tds[1].i.string.strip()
    else:
        real_name = tds[1].text.strip()

    note = tds[2].text.rstrip()
    if '[' in note:
        idx = note.find("[")
        # print(f'{note.find("[")}')
        # print(f'idx: {idx}')
        notes += (note[0: int(idx)])
    elif tds[2].a and ('[' not in tds[2].a.string):
        notes += tds[2].a.string
    else:
        notes += note


    ct_count += 1

    print(f'{name} | {real_name} | {notes}')

print(f'\nTotal Creative team Count: {ct_count}\n')


print(f'{rosters[14]}')
pat = '-'*len(rosters[14])
print(f'{pat}')


print(f'Name {space} | {space} Notes')
md_count = 0
trs = tables[24].find_all('tr')
for i in range(1, len(trs)):
    name=notes=''

    tds = trs[i].find_all('td')
    if tds[0].a:

        name = tds[0].text
        idx = name.find('[')
        name = name[0: int(idx)]
    '''
    else:
        name = tds[0].text.rstrip()

    if tds[1].span and not tds[1].i:
        real_name = tds[1].span.string.rstrip()
    elif tds[1].i:
        real_name = tds[1].i.string.strip()
    else:
        real_name = tds[1].text.strip()
    '''
    note = tds[1].text.rstrip()
    if '[' in note:
        idx = note.find("[")
        # print(f'{note.find("[")}')
        # print(f'idx: {idx}')
        notes += (note[0: int(idx)])
    elif tds[1].a and ('[' not in tds[1].a.string):
        notes += tds[1].a.string
    else:
        notes += note

    md_count += 1

    print(f'{name} | {notes}')

print(f'\nTotal Music Department Count: {md_count}\n')


print(f'{rosters[15]}')
pat = '-'*len(rosters[15])
print(f'{pat}')

print(f'{header}')

p_count = 0
trs = tables[25].find_all('tr')
for i in range(1, len(trs)):
    name=real_name=notes=''

    tds = trs[i].find_all('td')
    if tds[0].a:

        name = tds[0].text
        idx = name.find('[')
        name = name[0: int(idx)]

    else:
        name = tds[0].text.rstrip()

    if tds[1].span and not tds[1].i:
        real_name = tds[1].span.string.rstrip()
    elif tds[1].i:
        real_name = tds[1].i.string.strip()
    else:
        real_name = tds[1].text.strip()

    note = tds[2].text.rstrip()
    if '[' in note:
        idx = note.find("[")
        # print(f'{note.find("[")}')
        # print(f'idx: {idx}')
        notes += (note[0: int(idx)])
    elif tds[2].a and ('[' not in tds[2].a.string):
        notes += tds[2].a.string
    else:
        notes += note


    p_count += 1

    print(f'{name} | {real_name} | {notes}')

print(f'\nTotal Producers Count: {p_count}\n')

print(f'{rosters[16]}')
pat = '-'*len(rosters[16])
print(f'{pat}')

print(f'{header}')

pc_count = 0
trs = tables[26].find_all('tr')
for i in range(1, len(trs)):
    name=real_name=notes=''

    tds = trs[i].find_all('td')
    if tds[0].a:

        name = tds[0].text
        idx = name.find('[')
        name = name[0: int(idx)]

    else:
        name = tds[0].text.rstrip()

    if tds[1].span and not tds[1].i:
        real_name = tds[1].span.string.rstrip()
    elif tds[1].i:
        real_name = tds[1].i.string.strip()
    else:
        real_name = tds[1].text.strip()

    note = tds[2].text.rstrip()
    if '[' in note:
        idx = note.find("[")
        # print(f'{note.find("[")}')
        # print(f'idx: {idx}')
        notes += (note[0: int(idx)])
    elif tds[2].a and ('[' not in tds[2].a.string):
        notes += tds[2].a.string
    else:
        notes += note


    pc_count += 1

    print(f'{name} | {real_name} | {notes}')

print(f'\nTotal WWE Performance Center Staff Count: {pc_count}\n')

print(f'{rosters[17]}')
pat = '-'*len(rosters[17])
print(f'{pat}')

print('Board of Directors and executive officers')
pat = '-'*len('Board of Directors and executive officers')
print(f'{pat}')

print(f'Name {space}|{space} Notes')
cstaff_count = 0
trs = tables[27].find_all('tr')
for i in range(1, len(trs)):
    name=notes=''

    tds = trs[i].find_all('td')
    if tds[0].a:

        name = tds[0].text
        idx = name.find('[')
        name = name[0: int(idx)]
    '''
    else:
        name = tds[0].text.rstrip()

    if tds[1].span and not tds[1].i:
        real_name = tds[1].span.string.rstrip()
    elif tds[1].i:
        real_name = tds[1].i.string.strip()
    else:
        real_name = tds[1].text.strip()
    '''
    note = tds[1].text.rstrip()
    if '[' in note:
        idx = note.find("[")
        # print(f'{note.find("[")}')
        # print(f'idx: {idx}')
        notes += (note[0: int(idx)])
    elif tds[1].a and ('[' not in tds[1].a.string):
        notes += tds[1].a.string
    else:
        notes += note

    cstaff_count += 1

    print(f'{name} | {notes}')

print(f'\nTotal Corporate staff count: {cstaff_count}\n')

print('Senior Management')
pat = '-'*len('Senior Management')
print(f'{pat}')

sm_count = 0
trs = tables[28].find_all('tr')
for i in range(1, len(trs)):
    name=notes=''

    tds = trs[i].find_all('td')
    if tds[0].a:

        name = tds[0].text
        idx = name.find('[')
        name = name[0: int(idx)]
    '''
    else:
        name = tds[0].text.rstrip()

    if tds[1].span and not tds[1].i:
        real_name = tds[1].span.string.rstrip()
    elif tds[1].i:
        real_name = tds[1].i.string.strip()
    else:
        real_name = tds[1].text.strip()
    '''
    note = tds[1].text.rstrip()
    if '[' in note:
        idx = note.find("[")
        # print(f'{note.find("[")}')
        # print(f'idx: {idx}')
        notes += (note[0: int(idx)])
    elif tds[1].a and ('[' not in tds[1].a.string):
        notes += tds[1].a.string
    else:
        notes += note

    sm_count += 1

    print(f'{name} | {notes}')

print(f'\nTotal Senior Management count: {sm_count}\n')



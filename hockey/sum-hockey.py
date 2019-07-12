#!/usr/bin/env python3

file = open('hockey-team-names.txt', 'r')
path = '/Users/dichharai/Documents/hackathon/athletes/hockey'

file_names = file.readlines()
goal_tenders_count = 0
skater_count = 0
# print(file_names)


for name in file_names:
    target_f = open(path + '/' + name.rstrip(), 'r')

    contents = target_f.readlines()
    for content in contents:
        if 'Total Goaltenders:' in content:
            goal_tenders_count += int(content[content.index(': ')+1: len(content.rstrip())])
    target_f.close()

    if 'Total Skaters:' in content:
            skater_count += int(content[content.index(': ')+1: len(content.rstrip())])

file.close()
print(f'Total Goaltenders: {goal_tenders_count}')
print(f'Total Skaters: {skater_count}')


'''
import os
path = '/Users/dichharai/Documents/hackathon/athletes/hockey'

#files  = []

for r, d, f in os.walk(path):
    for file in f:
        #files.append(os.path.join(file))
        print(f'{file}')

'''

#!/usr/bin/env python3

file = open('soccer-team-names.txt', 'r')
path = '/Users/dichharai/Documents/hackathon/athletes/soccer/male-soccer-teams'

file_names = file.readlines()
total_player = 0

for name in file_names:
    # target_f = reversed(list(open(path + name.rstrip(), 'r')))
    #print(name)

    target_f = open(path + '/' + name.rstrip(), 'r')
    contents = target_f.readlines()

    for content in contents:
        if 'Total player' in content:
            total_player += int(content[content.index(': ')+1: len(content.rstrip())])


file.close()
print(f'Total Soccer player: {total_player}')

'''
import os
path = '/Users/dichharai/Documents/hackathon/athletes/soccer/male-soccer-teams/'

for r, d, f in os.walk(path):
    for file in f:
        print(f'{file}')
'''
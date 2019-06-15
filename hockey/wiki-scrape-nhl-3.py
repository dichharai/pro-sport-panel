#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

file = open('nhl-links.txt', 'r')
lines = file.readlines()
# print(lines[3])
link1 = lines[4].strip()
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

w_file.close()
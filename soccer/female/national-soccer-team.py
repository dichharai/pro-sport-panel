#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

website_content = requests.get('https://en.wikipedia.org/wiki/United_States_women%27s_national_soccer_team').text
soup = BeautifulSoup(website_content, 'lxml')

title = soup.title.string.rstrip()
pat = '-'*len(title)
print(title)
print(pat)


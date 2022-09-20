#!hfunctio/bin/python

import sys
from bs4 import BeautifulSoup
import os
import time


def financial(ticker, row):
    url = 'https://finance.yahoo.com/quote/' + ticker + '/financials'
    os.system(f'curl {url} &> tmp')
    with open('tmp', 'r') as file:
        page = file.readlines()
    page = ''.join(page)
    os.system('rm -rf tmp')
    page_parsed = BeautifulSoup(page, 'html.parser')
    if page_parsed.title is None:
        raise Exception('Wrong ticker')
    tags = page_parsed.find_all(attrs={'data-test': 'fin-row'})
    rows = [tag.find(class_='Va(m)').get_text() for tag in tags]
    if row not in rows:
        raise Exception('Error with row')
    elems = tags[rows.index(row)].find_all('span')
    return tuple(elem.get_text() for elem in elems)


if __name__ == '__main__':
    if len(sys.argv) == 3:
        print(financial(sys.argv[1], sys.argv[2]))

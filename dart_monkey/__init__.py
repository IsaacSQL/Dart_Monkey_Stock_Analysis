import bs4 as bs
import os
import requests
import time
from .MonkeySee import MonkeySee
from .options import options

def TickerGrabber():
    resp = requests.get('https://en.wikipedia.org/wiki/Russell_1000_Index')
    soup = bs.BeautifulSoup(resp.text, 'lxml')
    table = soup.find('table', {'class': 'wikitable sortable'})

    ticker = []
    tickers = []
    for row in table.findAll('tr')[1:]:
        ticker = row.findAll('td')[1].text
        tickers.append(ticker)
    tickers = [s.replace('\n', '') for s in tickers]
    return tickers

def main():
    print(""" Dart_Monkey 2024
            _   
        _ \'-_,#
        _\'--','`|
        \`---`  /
        `----'`
        """)
    time.sleep(0.5)
    print("Beginning Data Scrape")
    # Create the output directory if it doesn't exist
    if not os.path.exists('output'):
        os.makedirs('output')
    args = options() # Args contains command line arguments
    tickers = []    
    tickers = TickerGrabber()
    for ticker in tickers:
        info = MonkeySee(ticker)
        info.toJSON()

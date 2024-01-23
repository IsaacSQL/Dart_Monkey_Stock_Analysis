import bs4 as bs
import os
import requests
import time
from .MonkeySee import MonkeySee
from .options import options

def TickerGrabber(stockindex, num):
    resp = requests.get(stockindex)
    soup = bs.BeautifulSoup(resp.text, 'lxml')
    table = soup.find('table', {'class': 'wikitable sortable'})

    ticker = []
    tickers = []
    for row in table.findAll('tr')[num:]:
        ticker = row.findAll('td')[num].text
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
    
    stockindex, num = '', 0
    if args.index == 'sp500':
        stockindex, num = 'https://en.wikipedia.org/wiki/S%26P_100', 0
    elif args.index == 'russell1000':
        stockindex, num = 'https://en.wikipedia.org/wiki/Russell_1000_Index', 1
    else:
        print(f'{args} is not a valid input. Try sp500, or russell1000')

    tickers = []    
    tickers = TickerGrabber(stockindex, num)
    for ticker in tickers:
        info = MonkeySee(ticker)
        info.toJSON()

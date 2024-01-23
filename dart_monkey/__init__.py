import yfinance as yahooFinance
import bs4 as bs
import requests
import time
import json
import os
from .MonkeySee import MonkeySee
from .options import options


# Set the ticker
#ticker = input('input ticker symbol: ')
def GetInformation(ticker):
    information = yahooFinance.Ticker(ticker)
    def Scraper(kpi, retry=0):
        try:
            result = information.info[kpi]
        except:
            if (retry < 2):
                retry += 1
                time.sleep(0.5)
                return Scraper(kpi, retry)
            else:
                result = 0
        return result
    return Scraper

def MonkeySee(ticker):
    Scraper = GetInformation(ticker)
    #assign KPIs
    Sector = Scraper('sector')
    PriceEarningsRatio = float(Scraper('trailingPE'))
    PriceEarningsGrowth = float(Scraper('pegRatio'))
    Beta = float(Scraper('beta'))
    ForwardPE = float(Scraper('forwardPE'))
    PriceToBook = float(Scraper('priceToBook'))
    MarketCap = float(Scraper('marketCap'))
    RetrunOnEquity = float(Scraper('returnOnEquity'))
    DebtToEquity = float(Scraper('debtToEquity'))
    EarningsPerShare = float(Scraper('trailingEps'))
    PriceToSales = float(Scraper('priceToSalesTrailing12Months'))
    DividendYield = float(Scraper('dividendRate'))

    # Data to be written
    data = {
        "name": ticker,
        "Sector": Sector,
        "PriceToEarningsRatio": PriceEarningsRatio,
        "PriceToEarningsGrowth": PriceEarningsGrowth,
        "Beta": Beta,
        "ForwardPE": ForwardPE,
        "PriceToBookRatio": PriceToBook,
        "MarketCapitalization": MarketCap,
        "ReturnOnEquity": RetrunOnEquity,
        "DebtToEquity": DebtToEquity,
        "EarningsPerShare": EarningsPerShare,
        "PriceToSales": PriceToSales,
        "Dividends": DividendYield
    }

    # Writing to sample.json
    with open(f'output/{ticker}.json', 'w') as f:
        json.dump(data, f)
    print(f'Finished Scraping {ticker} Data')

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
    MonkeySee(ticker)

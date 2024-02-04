import bs4 as bs
import os
import requests
import time
import pandas as pd
import json
from .MonkeySee import MonkeySee
from .options import options

def TickerGrabber(stockindex, num):
    resp = requests.get(stockindex)
    soup = bs.BeautifulSoup(resp.text, 'lxml')
    table = soup.find('table', {'class': 'wikitable sortable'})

    ticker = []
    tickers = []
    for row in table.findAll('tr')[1:]:
        ticker = row.findAll('td')[num].text
        tickers.append(ticker)
    tickers = [s.replace('\n', '') for s in tickers]
    return tickers
def scrape(args):
    stockindex, num = '', 0
    if args.index == 'sp500':
        stockindex, num = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies', 0
    elif args.index == 'russell1000':
        stockindex, num = 'https://en.wikipedia.org/wiki/Russell_1000_Index', 1
    else:
        print(f'{args} is not a valid input. Try sp500, or russell1000')
        return 1
    print("Beginning Data Scrape")
    tickers = []    
    tickers = TickerGrabber(stockindex, num)
    for ticker in tickers:
        info = MonkeySee(ticker)
        info.toJSON()

def main():
    print(""" Dart_Monkey 2024
         _   
       _ \'-_,#
      _\'--','`|
      \`---`  /
       `----'`
        """)
    time.sleep(0.5)
    # Create the output directory if it doesn't exist
    if not os.path.exists('output'):
        os.makedirs('output')
    
    args = options() # Args contains command line arguments
    
    if args.noscrape:
        scrape(args)
    
    print("Beginning Data Analysis")
    # Initialize an empty DataFrame
    df = pd.DataFrame()
    # Specify the directory containing the JSON files
    directory = os.path.join(os.getcwd(), 'output')
    # add the data from all the JSON files to df
    for filename in os.listdir(directory):
        if filename.endswith('.json'):  # Check if the file is a JSON file
            with open(os.path.join(directory, filename)) as f:
                data = json.load(f)  # Load the JSON file
                temp_df = pd.DataFrame(data, index=[0])  # Convert the dictionary to a DataFrame
                df = df._append(temp_df, ignore_index=True)  # Append the data to the main DataFrame
    #clean empty data
    df.drop(df[(df.iloc[:, 1:] == 0).all(axis=1)].index, inplace=True)
    
    ratioList = ['PriceToEarningsRatio', 'PriceToEarningsGrowth', 'ForwardPE', 'PriceToBookRatio', 'MarketCapitalization', 'ReturnOnEquity', 'ReturnOnEquity', 'DebtToEquity', 'EarningsPerShare', 'PriceToSales', 'Dividends']
    for ratio in ratioList:
        max = MonkeySee.get_max(ratio, df)
        MonkeySee.rank(ratio, max, df)

    df['sum'] = df[['PriceToEarningsRatio ranking', 'PriceToEarningsGrowth ranking', 'ForwardPE ranking', 'PriceToBookRatio ranking', 'MarketCapitalization ranking', 'ReturnOnEquity ranking', 'ReturnOnEquity ranking', 'DebtToEquity ranking', 'EarningsPerShare ranking', 'PriceToSales ranking', 'Dividends ranking']].sum(axis=1)
    df.sort_values(by=['sum'])
    max_index = df['sum'].idxmax()
    overall = df.loc[max_index, 'name']
    min_index = df['sum'].idxmin()
    worst = df.loc[min_index, 'name']
    random_row = df.sample()
    random_element = random_row['name'].values[0]
    print(f"""Top: {overall}
    Bottom: {worst}
    Dart: {random_element}""")
    df.to_csv('output.csv', index=False)

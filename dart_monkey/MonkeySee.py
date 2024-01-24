import yfinance as yahooFinance
import time
import json
class MonkeySee:
    def __init__(self, ticker):
        self.ticker = ticker
    # Set the ticker
    #ticker = input('input ticker symbol: ')
    def GetInformation(self):
        information = yahooFinance.Ticker(self.ticker)
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
    
    def toJSON(self):
        Scraper = self.GetInformation()
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
            "name": self.ticker,
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
        with open(f'output/{self.ticker}.json', 'w') as f:
            json.dump(data, f)
        print(f'Finished Scraping {self.ticker} Data')
    def get_max(column_name, df):
        # Replace 'inf' with 0 in the column
        df[column_name] = df[column_name].replace(float('inf'), 0)
        max_value = df[column_name].max()
        return max_value
    def rank(column_name, max_divisor, df):
            # Sorting by column values
            df.sort_values(by=[column_name])
            # Create a new column
            df[str(f'{column_name} ranking')] = df[str(column_name)] / max_divisor

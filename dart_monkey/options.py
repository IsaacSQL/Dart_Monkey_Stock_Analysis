import argparse

def options():
    # Create parser
    parser = argparse.ArgumentParser(
        description='Scrape data about stocks',
        prog='dart_monkey',
        usage='''py -m dart_monkey [INDEX]
        Index should be sp500 for the S&P 500 or russell1000 for Russell 1000
        '''
    )
    # Set options for scraper
    parser.add_argument(
        'index',
        metavar='INDEX',
        help='sp500 or russell1000',
        type=str
    )

    parser.add_argument(
        '--noscrape',
        help='Disable scraping',
        action='store_false'
    )
    return parser.parse_args()

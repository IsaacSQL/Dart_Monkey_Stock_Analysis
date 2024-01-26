# Description
Dart Monkey 2024.
This is a project related to ongoing financial data analysis and data scraping I am experimenting with.
When run, the project will pull KPIs from the stocks on the Russel 1,000 or S&P500 Index. These will be output into separate JSON files.
A basic form of analysis is now run on the scraped data. The final output is a top, bottom, and random stock. The data is exported to a CSV for easy review.

Format is `py -m dart_monkey INDEX`. Index should be `sp500` for the S&P 500 or `russell1000` for Russell 1,000 index
# Options
`--noscrape` disables the data scrape and uses existing files in the output folder

# Disclaimer
I have heard that data from yahoo finance is not the most reliable or up to date, this program is intended for educational purposes only.

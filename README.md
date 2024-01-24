# Description
Dart Monkey 2024.
This is a project related to ongioing financial data analysis and data scraping I am ecperimenting with.
The initial project is very simple to usem but has limited options for data scraping and can be a little cluttered in its output.
When run, the project will pull KPIs from the stocks on the Russel 1,000 Index. These will be output into seperate JSON files named {Ticker}.json.

Format is `py -m dart_monkey INDEX`. Index should be `sp500` for the S&P 500 or `russell1000` for Russell 1,000 index
# Options
`--noscrape` disables the data scrape and uses existing files in the output folder

# Disclaimer
I have heard that data from yahoo finance is not the most reliable or up to date, this program is intended for educational purposes only.

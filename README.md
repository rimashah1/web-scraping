# web-scraping
Uses beautifulsoup4 to web scrape

# Packages required
To run both .py files the pandas, beautifulsoup4, and requests package is required.

# webscraping1.py
The first file extracts a list of brittanica's best books ever written. The book titles were extracted with the 'h2' html tag. 

# webscraping2.py
The second file extracts the trending stocks from Yahoo Finance. The symbol and last price of each trending stock was scraped. The symbols were extracted with 'td', class_='data-col0 Ta(start) Pstart(6px) Pend(15px)' and the last price was scraped with 'td', class_='data-col2 Ta(end) Pstart(20px)'



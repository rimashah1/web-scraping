import requests
from bs4 import BeautifulSoup
import pandas as pd


page = requests.get('https://finance.yahoo.com/lookup/')

# create a BeautifulSoup object
soup = BeautifulSoup(page.text, 'html.parser')

# print pretty
print(soup.prettify())



############################
# scraping the stock symbols
############################

# use soup to find all data of interest
symbol = soup.find_all('td', class_='data-col0 Ta(start) Pstart(6px) Pend(15px)')

symbols = []
for i in symbol:
    name = i.text                 ## changes info into text
    name = name.strip()           ## clean name remove whitespace
    name = name.replace('\n','')  ## remove new line
    symbols.append(name)          ## save into list
symbols



###############################
# scraping the stock last price
###############################

last_price = soup.find_all('td', class_='data-col2 Ta(end) Pstart(20px)')

last_prices = []
for i in last_price:
    name = i.text 
    name = name.strip()           
    name = name.replace('\n','')  
    last_prices.append(name)
last_prices



# save both lists into dataframe
stocks = pd.DataFrame({'Symbol': symbols, 'Last Price': last_prices})

# save df as .csv
stocks.to_csv("C:/Users/Rima/GitHub/web-scraping/data/stocks.csv")
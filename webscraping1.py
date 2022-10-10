import requests
from bs4 import BeautifulSoup
import pandas as pd

# use requests to get url
page = requests.get('https://www.britannica.com/list/12-novels-considered-the-greatest-book-ever-written')

# create a BeautifulSoup object
soup = BeautifulSoup(page.text, 'html.parser')

# print pretty
print(soup.prettify())



######################
# scraping book titles
######################

# use soup to find all data of interest
bestbooks = soup.find_all('h2')

# edit the extracted info to be readable
bestbooks_list = []
for i in bestbooks:
    name = i.text                 ## changes info into text 
    name = name.strip()           ## clean name remove whitespace
    name = name.replace('\n','')  ## remove new line
    bestbooks_list.append(name)   ## add edited info to list
bestbooks_list



# put list into a dataframe
books2read = pd.DataFrame({'Book Names':bestbooks_list})

# save as .csv
books2read.to_csv("C:/Users/Rima/GitHub/web-scraping/data/books2read.csv")
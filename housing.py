import requests
import xlwt
import pandas as pd

from bs4 import BeautifulSoup
from selenium import webdriver

#website where we get our source data
url = "https://www.car.org/marketdata/data/countysalesactivity"

#set up 
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

#the entire table
table = soup.find("table", class_ = "responsive")
rowValues = []
for row in table.select('tr'):
    #td is each indiviual value in the row
    tds = row.find_all('td')
    values = []
    for td in tds:
        values.append(td.text.strip())
    rowValues.append(values)
df = pd.DataFrame(rowValues)
print(df)
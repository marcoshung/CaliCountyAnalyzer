import requests
import xlwt

import pandas as pd
pd.set_option('display.max_columns', None)  

from bs4 import BeautifulSoup
from selenium import webdriver

#validates argument for later use
def isValidCounty(county):
    f = open("county list", 'r')
    allnames = []
    name = f.readline()
    while name:
        allnames.append(name.strip().lower())
        name = f.readline()
    if (county.lower() + " county") in allnames:
        return True
    return False



#website where we get our source data
url = "https://www.car.org/marketdata/data/countysalesactivity"

#set up 
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

#the entire table
table = soup.find("table", class_ = "responsive")
county = []
housingprice = []
for row in table.select('tr'):
    #td is each indiviual value in the row
    tds = row.find_all('td')
    if '$' in tds[1].text.strip() and isValidCounty(tds[0].text.strip()):
        county.append(tds[0].text.strip())
        housingprice.append(tds[1].text.strip())

#Read unlisted counties & housing prices
unlistedprices = open("UnlistedHousingPrices.txt", "r")
line  = unlistedprices.readline()
while line:
    values = line.split()
    county.append(values[0])
    housingprice.append(values[1])
    line = unlistedprices.readline()
datavalues = {"County Name" : county, "Housing Price" : housingprice}
df = pd.DataFrame(datavalues)
export_csv = df.to_csv (r'/Users/marcoshung/eclipse-workspace/CaliCountyAnalyzer/housingdata.csv', index = None, header=True)
#print(df)

import requests
import pandas as pd
pd.set_option('display.max_columns', None)  

from bs4 import BeautifulSoup
from selenium import webdriver

#validates argument for later use
def isValidCounty(county):
    f = open("countylist", 'r')
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

datavalues = {"County Name" : county, "Housing Price" : housingprice}
df = pd.DataFrame(datavalues)
export_csv = df.to_csv (r'/Users/marcoshung/eclipse-workspace/CaliCountyAnalyzer/test.csv', index = None, header=True)
#print(df)

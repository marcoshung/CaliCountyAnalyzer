# creates a .txt file with all county names for easy access
import requests
import xlwt
import pandas as pd

from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/List_of_counties_in_California"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

table = soup.find("table", style = "text-align: center;")
counties = []
population = []
for row in table.select('tr'):
    name = row.find_all('th')
    tds = row.find_all('td')
    print(type(tds))
    for n in name:
        if "county" in n.text.lower():
            counties.append(n.text.strip())
   

#ignore first two data, bc they are titles
counties.pop(0)
counties.pop(0)
print(counties)
datafile = open("county list", "w+")

for name in counties:
    datafile.write(name + "\n")
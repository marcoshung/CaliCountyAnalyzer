import requests
import xlwt

import pandas as pd
pd.set_option('display.max_columns', None)  

from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/List_of_California_locations_by_income"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

tables = soup.find_all("table")
counties = []
population = []
populationdensity = []
income = []
incomeTable = tables[1].select('tr')
#empty row
incomeTable.pop(0)
for row in incomeTable:
    values = row.find_all('td')
    line = ""

    counties.append(values[0].text)
    population.append(values[1].text)
    populationdensity.append(values[2].text)
    income.append(values[4].text)


datavalues = {"County": counties, "Population" :population, "Population Density":populationdensity, "Average Household Income" :income}
df = pd.DataFrame(datavalues)
export_csv = df.to_csv (r'/Users/marcoshung/eclipse-workspace/CaliCountyAnalyzer/incomeandpopdata.csv', index = None, header=True)

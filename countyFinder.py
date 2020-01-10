#Creates a field with all counties in California
#Also creates a .txt file for easy access
import requests
import xlwt
import pandas as pd

from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/List_of_counties_in_California"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

table = soup.find("table")
for row in table.select('tr'):
    name = row.find_all('th')
    for n in name:
        print(n.text)
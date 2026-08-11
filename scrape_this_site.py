import csv
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

url = "https://www.scrapethissite.com/pages/simple/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/120.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(url, headers=headers)
#print(response.status_code)

soup=BeautifulSoup(response.text,"lxml")
#print(soup)

box=soup.find_all("h3",class_="country-name")
#print(box)

countries=[]
for b in box:
    country=b.text.strip()
    countries.append(country)
#print(countries)



tox=soup.find_all("span",class_="country-capital")
#print(tox)
capitals=[]
for t in tox:
    capital=t.text
    capitals.append(capital)
#print(capitals)


dox=soup.find_all("span",class_="country-population")
#print(dox)
population=[]
for d in dox:
    populations=d.text
    population.append(populations)
#print(population)



df=pd.DataFrame({
    "Country":countries,
    "Capital":capitals,
    "Population":population
})
print(df)

df.to_csv("capital_data.csv")







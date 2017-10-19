from bs4 import BeautifulSoup
import re
import requests
import grequests
import pandas as pd
import json


url = requests.get('https://www.leboncoin.fr/voitures/1316814811.htm?ca=21_s')
soup = BeautifulSoup(url.content, 'lxml')

valeurs = [i.get_text() for i in soup.find_all('span', class_='value')]

#creation de la DataFrame
df = pd.DataFrame(dict(version=version, annee=annee, km=km, prix=prix))
print(df)
#data = soup.find('body').find_all('script')[3].string
#jsonValue = '{%s}' % (data.split('{', 1)[1].rsplit(}', 1)[0],)
#value = json.loads(jsonValue)

import pandas as pd
import requests
import grequests
from bs4 import BeautifulSoup

# requetes multiples sur plusieurs pages Zoe
urls = []
debut = 'https://www.leboncoin.fr/voitures/offres/provence_alpes_cote_d_azur/?th='
fin = '&q=zo%E9'
for i in range(1,10):
    r = requests.get(debut+str(i)+fin).status_code
    if r == 200:
        urls.append(debut+str(i)+fin)
    else:
        break

unsent_request = (grequests.get(url) for url in urls)
results = grequests.map(unsent_request)

# recuperation de tous les urls des differentes Zoe
soup_url = []
for i in range(0,9):
    soup_url.append(BeautifulSoup(results[i].content, 'lxml')).find('a', 'href')
print(soup_url)

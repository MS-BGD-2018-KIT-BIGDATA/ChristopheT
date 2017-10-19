import bs4
import re
import requests
import grequests
import pandas as pd

# Test sur la region PACA
liste_urls = []
debut = 'https://www.leboncoin.fr/voitures/offres/provence_alpes_cote_d_azur/?th='
fin = '&q=zo%E9'
for i in range(1,10):
    r = requests.get(debut+str(i)+fin).status_code
    if r == 200:
        liste_urls.append(debut+str(i)+fin)
    else:
        break

unsent_request = [grequests.get(url) for url in liste_urls]
results = grequests.map(unsent_request)
#html_page = requests.get("https://www.leboncoin.fr/voitures/offres/provence_alpes_cote_d_azur/?o=1&q=zoe")
urls = []
for p in range(0,1):
    soup = bs4.BeautifulSoup(results[p].content, 'lxml')
    soup = soup.find('section', class_= "tabsContent block-white dontSwitch")
    for page in soup.find_all('a'):
        urls.append(page.get('href'))

soupir = []
for x in urls:
    requests.get('x')
    soupir.append(bs4.BeautifulSoup(x.content, 'lxml'))
valeurs = [i.get_text() for i in soup.find_all('span', class_='value')]
version = valeurs
annee = valeurs.map(lambda, range(3:100:5))
km = valeurs
prix = valeurs
#creation de la DataFrame
df = pd.DataFrame({
"version": version,
"annee": annee,
"km": km,
"prix": prix
})
print(df)
#data = soup.find('body').find_all('script')[3].string
#jsonValue = '{%s}' % (data.split('{', 1)[1].rsplit(}', 1)[0],)
#value = json.loads(jsonValue)

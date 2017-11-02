import urllib
import bs4
import collections
import pandas as pd
import requests

data_json = requests.get('https://open-medicaments.fr/api/v1/medicaments?query=ibuprofene').json()
# on va chercher tous les IDS de chacun des medicaments
data_json = pd.DataFrame(data_json)
data_test = requests.get('https://open-medicaments.fr/api/v1/medicaments/64565560').json()
print(data_json)




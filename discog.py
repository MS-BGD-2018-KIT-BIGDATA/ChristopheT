#tests webscraping, API du site www.discogs.com
import pandas as pd
import requests
from bs4 import BeautifulSoup
import numpy as np
import re
import discogs_client


# Comparaison - recuperation de la discographie soit par scraping soit via l'API du site
#token hoLtgcULeRfSKyRTtWZdHfVODuXVOJRAbeXoKOtV

#apidiscog = requests.get("https://api.discogs.com/oauth/hoLtgcULeRfSKyRTtWZdHfVODuXVOJRAbeXoKOtV")
d = discogs_client.Client('ExampleApplication/0.1', user_token="hoLtgcULeRfSKyRTtWZdHfVODuXVOJRAbeXoKOtV")
results = d.search('Eclipce', type='release')
print(d.release(8593477))

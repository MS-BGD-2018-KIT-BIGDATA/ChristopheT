from bs4 import BeautifulSoup
import requests
from urllib2 import urlopen

prix = urlopen('https://www.cdiscount.com/search/10/acer+pc+portable.html#_his_').read()
soup = BeautifulSoup(prix, 'lxml')
for i in soup.find_all('span', {'class':'ecoBlk'}):
    print i.text



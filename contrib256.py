##recuperer les 256 plus gros contributeurs sur la page github: (https://gist.github.com/paulmillr/2657075)
## https://developer.github.com/v3/ (pour info, API github)

import requests
from bs4 import BeautifulSoup

## debut
page_git = requests.get('https://gist.github.com/paulmillr/2657075')
soup = BeautifulSoup(page_git.content, 'html.parser')
noms = soup.find('table', attrs = {'cellspacing' : '0'}).find_all('a')
for pseudo in noms:
    print(pseudo.text) ## liste de tous les contributeurs

## --> on selectionne uniquement les 256 plus gros contributeurs
big_contrib = pseudo.text[0:255]
print(big_contrib)

## --> recuperer le nombre moyen de stars par repos et par utilisateur

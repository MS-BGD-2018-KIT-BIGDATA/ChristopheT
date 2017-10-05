##recuperer les 256 plus gros contributeurs sur la page github: (https://gist.github.com/paulmillr/2657075)
## https://developer.github.com/v3/ (pour info, API github)

import requests
import numpy as np
from bs4 import BeautifulSoup
import json

## debut
page_git = requests.get('https://gist.github.com/paulmillr/2657075')
soup = BeautifulSoup(page_git.content, 'html.parser')
noms = soup.find('table', attrs = {'cellspacing' : '0'}).find_all('a')
for pseudo in noms:
    print(pseudo.text) ## liste de tous les contributeurs

## --> on selectionne uniquement les 256 plus gros contributeurs
big_contrib = pseudo.text[0:255]

## --> recuperer le nombre moyen de stars par repos et par utilisateur
## via API github

r = requests.get(url='https://api.github.com/users/GrahamCampbell/repos') # Test sur le premier de la liste
data = r.json()
count = []
for i in range(0, len(data)):
    count.append(data[i]['stargazers_count'])
print(np.mean(count))

## Boucle for pour avoir les moyennes de 256 contributeurs
data = []
for noms in big_contrib:
    data = data.append(requests.get(url='https://api.github.com/users/' + str(big_contrib[noms]) + '/repos').json())

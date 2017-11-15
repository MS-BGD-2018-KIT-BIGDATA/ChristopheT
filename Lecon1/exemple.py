import urllib
import bs4
import collections
import pandas as pd
import requests


# pour le site que nous utilisons, le user agent de python 3 n'est pas  bien passé :
# on le change donc pour celui de Mozilla

req = urllib.request.Request('http://pokemondb.net/pokedex/national', headers = {'User-Agent' : 'Mozilla/5.0'})
html = urllib.request.urlopen(req).read()
page = bs4.BeautifulSoup(html, "lxml")

# récupérer la liste des noms de pokémon

liste_pokemon =[]
for pokemon in page.findAll('span', {'class' : 'infocard-tall'}) :
    pokemon = pokemon.find('a').get('href').replace("/pokedex/",'')
    liste_pokemon.append(pokemon)

## Fonction pour obtenir les caractéristiques de pokemons

def get_page(pokemon_name):
    url_pokemon = 'http://pokemondb.net/pokedex/'+ pokemon_name
    req = urllib.request.Request(url_pokemon, headers = {'User-Agent' : 'Mozilla/5.0'})
    html = urllib.request.urlopen(req).read()
    return bs4.BeautifulSoup(html, "lxml")


def get_cara_pokemon(pokemon_name):
    page = get_page(pokemon_name)
    data = collections.defaultdict()

    # table Pokédex data, Training, Breeding, base Stats

    for table in page.findAll('table', { 'class' : "vitals-table"})[0:4] :
        table_body = table.find('tbody')
        for rows in table_body.findChildren(['tr']) :
            if len(rows) > 1 : # attention aux tr qui ne contiennent rien
                column = rows.findChild('th').getText()
                cells = rows.findChild('td').getText()
                cells = cells.replace('\t','').replace('\n',' ')
                data[column] = cells
                data['name'] = pokemon_name
    return dict(data)

items = []
for e, pokemon in enumerate(liste_pokemon) :
    print(e, pokemon)
    item = get_cara_pokemon(pokemon)
    items.append(item)
    if e > 20:
        break
df = pd.DataFrame(items)
df.head()
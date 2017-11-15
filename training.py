# Entrainement webscraping et utilisation de regex
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

html=urlopen("https://jordsjo.bandcamp.com/album/songs-from-the-northern-wasteland-breidablik-jordsj-split-album")
bs0bj = BeautifulSoup(html, 'lxml')
title=bs0bj.find("h2", class_="trackTitle", itemprop="name").get_text()

print(title)


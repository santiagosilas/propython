# coding: utf-8
from requests import get
from bs4 import BeautifulSoup as BS

# url buscada
url = 'https://dataquestio.github.io/web-scraping-pages/ids_and_classes.html'

# hora da sopa ..
sopa = BS(get(url).content, 'html.parser')

# buscar pela classe
paragraphs = sopa.find_all(class_='outer-text')
print(paragraphs)

# buscar pelo o elemento e pela classe
paragraphs = sopa.find_all('p', class_='outer-text')
print(paragraphs)

# buscar pelo id
paragraphs = sopa.find_all(id='first')
print(paragraphs)

# buscar todos os parágrafos dentro de uma div
paragraphs = sopa.select('div p')
print(paragraphs)

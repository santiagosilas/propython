# coding: utf-8
import requests
from bs4 import BeautifulSoup as BS

# url a ser acessada
url = 'https://dataquestio.github.io/web-scraping-pages/simple.html'

# Obtém a página - Um objeto da classe <class 'requests.models.Response'>
pagina = requests.get(url)

# Vamos fazer uma sopa ..
sopa = BS(pagina.content, 'html.parser')

# obtém uma lista de tags elementos <p>
lista_parágrafos = sopa.find_all('p')

# O parágrafo
parágrafo = lista_parágrafos[0]
print(parágrafo)

# O conteúdo (texto) do parágrafo
conteúdo = parágrafo.get_text()
print(conteúdo)

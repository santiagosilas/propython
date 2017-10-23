# coding: utf-8
import requests
from bs4 import BeautifulSoup as BS

# url a ser acessada
url = 'https://dataquestio.github.io/web-scraping-pages/simple.html'

# Obtém a página - Um objeto da classe <class 'requests.models.Response'>
pagina = requests.get(url)

print('Página', pagina)
print('Página is an', type(pagina))
print('Status da Página:', pagina.status_code)

# Vamos fazer uma sopa ..
# Obtemos um objeto do tipo <class 'bs4.BeautifulSoup'>
sopa = BS(pagina.content, 'html.parser')

print(type(sopa))
print(sopa)

# Para exibir o conteúdo formatado corretamente
print(sopa.prettify())


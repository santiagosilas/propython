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

print('----------------')
for i, child in enumerate(sopa.children):
    print(i, type(child), child)

html = list(sopa.children)[2]

print('-------------')
for child in enumerate(html.children):
    print(type(child), child)

body = list(html.children)[3]

print(type(body))
print(body) 

children = list(body.children)
print(children)
p = children[1]
print(p)

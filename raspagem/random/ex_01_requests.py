# coding: utf-8
import requests

url = 'https://dataquestio.github.io/web-scraping-pages/simple.html'
pagina = requests.get(url)

print(pagina)
print(type(pagina))
print(pagina.status_code)
print(pagina.content)


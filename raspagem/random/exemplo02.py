from requests import get
from bs4 import BeautifulSoup

url = 'http://www.ifce.edu.br'

page = requests.get(url)
texto = page.content.decode('utf-8')

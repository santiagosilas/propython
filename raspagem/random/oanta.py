import requests
from bs4 import BeautifulSoup

page = requests.get('http://www.oantagonista.com')
soup = BeautifulSoup(page.content, 'html.parser')

articles = soup.find_all('article')
for index, article in enumerate(articles):
    title = article.find('h2').get_text()
    content = article.find('p').get_text()
    print(index, title)
    print(content)
    print('\n----\n')

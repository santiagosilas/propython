import urllib.request

url = 'http://www.ifce.edu.br'

# Obter o conteúdo da página
pagina = urllib.request.urlopen(url)
texto1 = pagina.read().decode('utf-8')

# Outra forma de fazer a mesma coisa ..
import requests
page = requests.get(url)
texto2 = page.content.decode('utf-8')

# Verificamos que todas as linhas são iguais 
print(texto1.split('\n') == texto2.split('\n'))
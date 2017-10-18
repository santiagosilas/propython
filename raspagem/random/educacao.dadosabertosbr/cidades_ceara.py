import urllib.request
import json

url = 'http://educacao.dadosabertosbr.com/api/cidades/ce'
cidades = urllib.request.urlopen(url).read()
cidades = json.loads(cidades.decode('utf-8'))

print('Lista de Cidades')
cidades = [print(cidade.split(':')[1]) for cidade in cidades]
print(cidades)

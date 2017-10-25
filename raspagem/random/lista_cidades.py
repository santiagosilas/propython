import requests, json

url = 'http://educacao.dadosabertosbr.com/api/cidades/ce'
cidades = requests.get(url).content
cidades = cidades.decode('utf-8')
cidades = json.loads(cidades)

for cidade in cidades:
	codigo, nome = cidade.split(':')
	print(nome)

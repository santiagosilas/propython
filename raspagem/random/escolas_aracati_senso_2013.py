import urllib.request
import json

#url = 'http://educacao.dadosabertosbr.com/api/cidades/ce'
#cidades = urllib.request.urlopen(url).read()
#cidades = json.loads(cidades.decode('utf-8'))

#print('Lista de Cidades')
#[print(cidade.split(':')[1]) for cidade in cidades]

print('Lista de Escolas Municipais de Aracati com Lab de Informática')
url = 'http://educacao.dadosabertosbr.com/api/escolas/buscaavancada?cidade=2301109&laboratorioInformatica=on&situacaoFuncionamento=1&dependenciaAdministrativa=3'

escolas = urllib.request.urlopen(url).read() # em bytes

# obtém uma lista de escolas
escolas = json.loads(escolas.decode('utf-8')) 

qtde, escolas = escolas

for escola in escolas:
	print(escola['nome'])

print('total:{0}\n'.format(len(escolas)))

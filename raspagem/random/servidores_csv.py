#coding: utf-8
import csv
from operator import itemgetter

arquivo = r'material\pt-2017-09-servs\20170930_Remuneracao.csv'

servidores = list()
ficheiro = open(arquivo, 'r')
reader = csv.reader(ficheiro)

count = 0
for linha in reader:
    count += 1
    if count == 1:
    	continue
    linha = list(linha[0].split('\t'))
    servidor = {'id':linha[2], 'cpf':linha[3], 'sal':float(linha[5]), 'nome':linha[4]}
    servidores.append(servidor)

servidores = sorted(servidores, key=itemgetter('sal'))
servidores.reverse()

for servidor in servidores[:10]:
	print('ID: {0}\tR$ {1}\tSERVIDOR:{2}'.format(servidor['id'], servidor['sal'], servidor['nome']))

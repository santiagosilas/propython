# coding:utf-8
import requests
from bs4 import BeautifulSoup as BS
from decimal import Decimal

# Portal da Transparência - Servidores IFCE
url_base = 'http://www.portaldatransparencia.gov.br/servidores/'
path_servidores = 'OrgaoExercicio-ListaServidores.asp?CodOS=15000&DescOS=MINISTERIO%20DA%20EDUCACAO&CodOrg=26405&DescOrg=INSTITUTO%20FEDERAL%20DO%20CEARA&Pagina={0}'

url_servidor = 'http://www.portaldatransparencia.gov.br/servidores/Servidor-DetalhaRemuneracao.asp?Op=2&IdServidor={0}&CodOrgao=26405&CodOS=15000&bInformacaoFinanceira=True'

def obter_pagina_servidores(numero_da_pagina):
    url = url_base + path_servidores.format(numero_da_pagina)
    pagina = requests.get(url)
    return pagina
    
def validar_pagina_servidores(pagina):
    msg = 'Par\\xe2metros de pesquisa inv\\xe1lido'
    if msg not in str(pagina.content):
        sopa = BS(pagina.content, 'html.parser')
        return sopa, True
    return None, False
    
def listar_servidores_pagina(sopa):
    listagem = sopa.find_all('table')[1]
    listagem = listagem.find_all('tr')[1:]

    servidores = list()
    for linha in listagem:
        tag_a = linha.find_all('a')[0]
        s_url = url_base + tag_a.attrs['href']
        s_id = s_url.split('&')[0].split('=')[1]
        s_url = s_url.format(s_id)
        servidores.append((s_id, s_url))
        
    return servidores
    
def obter_remuneracao_servidor(url_servidor):
    sopa_serv = BS(requests.get(url_servidor).content, 'html.parser')
    div_resumo = sopa_serv.find_all('div', id='resumo')[0]
    tag_a = div_resumo.find_all('a')[0]
    url_r = 'http://www.portaldatransparencia.gov.br' + tag_a.attrs['href']
    sopa_r = BS(requests.get(url_r).content, 'html.parser')
    '''
    Em div id='listagemConvenios', dentro de tbody, na 3 tr class="remuneracaodetalhe
    '''
    div_convenios = sopa_r.find_all('div', id='listagemConvenios')[0]
    tbody = div_convenios.find_all('tbody')[0]
    tr_rem = tbody.find_all('tr', class_='remuneracaodetalhe')[2]
    coluna_valor = tr_rem.find_all('td', class_='colunaValor')[0]
    valor = coluna_valor.get_text().replace('.', '').replace(',','.')
    return valor
    
def salvar_salarios_servidores():
    arquivo = open('servidores.txt', 'w')
    for numero_pagina in range(5000):
        pagina = obter_pagina_servidores(numero_pagina)
        sopa, success = validar_pagina_servidores(pagina)
        if success:
            lista = listar_servidores_pagina(sopa)
            print('total de servidores listados: {0}'.format(len(lista)))
            for servidor in lista:
                valor = obter_remuneracao_servidor(servidor[1])
                linha = '{0}, {1}\n'.format(servidor[0], valor)
                arquivo.write(linha)
                print(linha)
        else:
            break
    arquivo.close()
    print('arquivo gerado com sucesso!')
    
if __name__ == '__main__':
    salvar_salarios_servidores()
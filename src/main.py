
import os
import pandas as pd
from pathlib import Path
from dotenv import load_dotenv 
load_dotenv()
from meuPacote.atletas import BASE_DIR, getAge, getCountry, getMedal
from meuPacote.email import enviar_email

def main():
    file = BASE_DIR + '/data/nomesAtletas.xlsx'
    df = pd.read_excel(file)
    print (df)
    #5
    #a) crie uma lista com 100 nomes dos atletas contidas no arquivo nomesAtletas.xlsx
    nomes_atletas = df['nome'].tolist()
    print(nomes_atletas)

    #b) crie um DataFrame com as seguintes colunas: nome, idade, país e medalha
    #c)Use as funções fornecidas na pasta meuPacote e pegue as informações solicitadas dos 100 nomes]
    idades_lista = []
    pais_lista =[]
    medalhas_lista =[]

    for i in (nomes_atletas):
        age = getAge(i)
        idades_lista.append(age)
        country = getCountry(i)
        pais_lista.append(country)
        medal = getMedal(i)
        medalhas_lista.append(medal)

    df ['idade'] = idades_lista
    df ['pais'] = pais_lista
    df ['medalhas'] = medalhas_lista
    print(df)

    #d) Exposte esse dataframe final com todas as informações para um arquivo excel na pasta data com o nome listaFinal.xlsx
    df.to_excel(BASE_DIR + '/data/listaFinal.xlsx')

    #6
    #a) Quais são os atletas com mais de 30 anos e que ganharam medalha de ouro
    letra_a = df.loc[(df['idade'] > 30) & (df['medalhas'] == 'Gold'),'nome'].tolist()
    print(f'Nome dos atletas com mais de 30 anos e que ganharam medalha de ouro:')
    for atleta in letra_a:
        print(atleta)

    #b) Quantos atletas ganharam medalha do "United States"
    letra_b = df.loc[(df['pais'] == 'United States'),'nome'].tolist()
    print(f'Os atletas do Estados Unidos são: ')
    for atleta in letra_b:
        print(atleta)
    print(f'No total, foram {len(letra_b)} atletas')

    #c)Quem é o atleta mais velho que ganhou uma medalha de ouro e quantos anos ele tem?
    df_ouro = df.loc[(df['medalhas']=='Gold')]
    idade_maxima = df_ouro['idade'].max()
    letra_c = df_ouro.loc[(df_ouro['idade'] == idade_maxima),'nome'].tolist()
    nome_mais_velho = letra_c[0]
    print(f'O nome do atleta mais velho a ganhar medalha de ouro foi {nome_mais_velho} com {int(idade_maxima)} anos')

    #d)Quantos paises participaram das olimpiadas?
    letra_d = df['pais'].nunique()
    print(f'Ao todo, foram {letra_d} países')

    #7)Mande um email pelo servidor yahoo utilizando a biblioteca python-dotenv 
    #a) assunto do email: Prova AP2
    #b) mensagem:

    usuario = os.environ.get("YAHOO_USER") 
    senha = os.environ.get("YAHOO_PASSWORD")
    destinatario = 'lucasgomessr10@gmail.com'
    assunto = 'Prova AP2'
    mensagem = f''''
    i) Nome dos atletas com mais de 30 anos e que ganharam medalha de ouro:
{', '.join(letra_a)}

ii) Os atletas dos Estados Unidos são:
{', '.join(letra_b)}
No total, foram {len(letra_b)} atletas

iii) O nome do atleta mais velho a ganhar medalha de ouro foi {nome_mais_velho} com {int(idade_maxima)} anos

iv) Ao todo, foram {letra_d} países
    '''

    enviar_email(usuario,senha,destinatario,assunto,mensagem)


if __name__ == '__main__':
    main()

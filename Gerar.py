import pandas as pd
import random 
from datetime import datetime, timedelta 

#Função para gerar dados de vendas ficticios

def gerar_dados(num_linhas, in_min, in_max):
    produtos = ['Tupperware', 'Bombril', 'Xerox', 'Kodak']
    cidades = ['Orlando', 'Anahein', 'Franco da Rocha','Poá']
    cores_produtos = ['Tupperware':(31,222,214),'Bombril':(19,9,84),'Xerox':(231,178,164),'Kodak': (255,42,241)]
    dados = []        
    
    #in_min = 0 
    #in_max = 365
    
    for _ in range(num_linhas):
        produto = random.choice(produtos)
        cidade = random.choice(cidades)
        valor = round(random.uniform(50,500),2) 
        data = datetime.today() - timedelta(days=random.randint(in_min,in_max)) 
        cor = cores_produtos(produto)
        dados.append([produto, cidade, valor, data])
        return dados 

#Gerar 100 linhas de dados com intervalo de datas de 1 a 365 dias
dados_prontos = gerar_dados(100, 1, 365)

#Criar o dataframe (efetivamente a tabela)
df_vendas = pd.DataFrame(dados_prontos, columns=['Produto','Cidade','Valor','Data',])
#Salvando em csv
df_vendas.to_excel('vendas.xlsx', index=False, engine='openpyxl')

print("Deu tudo certo! O Arquivo foi salvo!")









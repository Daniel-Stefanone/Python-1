import pandas as pd
import random 
from datetime import datetime, timedelta

# Função para gerar dados de vendas fictícios
def gerar_dados(num_linhas, in_min, in_max):
    produtos = ['Tupperware', 'Bombril', 'Xerox', 'Kodak']
    cidades = ['Orlando', 'Anahein', 'Franco da Rocha', 'Poá']
    
    # Dicionário para associar cada produto a uma cor RGB
    cores_produtos = {
        'Tupperware': (255, 0, 0),  # Vermelho
        'Bombril': (0, 255, 0),     # Verde
        'Xerox': (0, 0, 255),       # Azul
        'Kodak': (255, 255, 0),     # Amarelo
    }
    
    dados = []
    for _ in range(num_linhas):
        produto = random.choice(produtos)
        cidade = random.choice(cidades)
        valor = round(random.uniform(50, 500), 2)
        data = datetime.today() - timedelta(days=random.randint(in_min, in_max))
        cor = cores_produtos[produto]  # Pega a cor RGB do produto escolhido
        dados.append([produto, cidade, valor, data, cor])  # Adiciona a cor aos dados
    return dados

# Gerar 100 linhas de dados com intervalo de datas de 1 a 365 dias
dados_prontos = gerar_dados(100, 1, 365)

# Criar o dataframe (efetivamente a tabela)
df_vendas = pd.DataFrame(dados_prontos, columns=['Produto', 'Cidade', 'Valor', 'Data', 'Cor'])

# Salvando em Excel (Arquivo .xlsx)
df_vendas.to_excel('vendas_com_cores.xlsx', index=False, engine='openpyxl')

print("Deu tudo certo! O Arquivo foi salvo como Excel com as cores RGB!")

from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt

#url da pagina alvo 

url ='https://www.themoviedb.org/movie'

#cabeçalho com user-agent para simular um navegador especifico 

headers0 = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36' } 

#fazendo a requisição com o cabeçalho e a url alvo

response = requests.get(url, headers=headers0)

#verificar nossa resposta foi positiva

if response.status_code == 403:
    print(f'Error {response.status_code}: Não autorizado')
elif response.status_code != 200:
    print(f'Error {response.status_code}: Não foi possível acessar a página')

#se passou daqui, deu tudo certo ao capturar a pagina, então vamos realizar o scrapping 
else:
    #realizar o parse no html
    soup = BeautifulSoup(response.text, "html.parser")
    print(soup.prettify()[:1000]) #mostra as 1000 linhas do html para entender a estrutura

#selecionando os filmes da pagina

movies = soup.find_all('div', class_='card style_1')
print(f'Total de Filmes:{len(movies)}')

movies_list = []
for movie in movies: 
    try:
        title_tag = movie.find('a', class_='image')
        
        nome_filme = title_tag['title'] if title_tag else 'titulo não encontrado'
        date_tag = movie.find('p')
        release_date = date_tag.get_text(strip=True) if date_tag else 'Data não encontrada'


        tabela = {"Título": nome_filme, "Data": release_date}
        
        movies_list.append(tabela)      
    
    except Exception as travou:
        print(f'Erro ao processar o filme: {travou}')
df = pd.DataFrame(movies_list)
if not df.empty:
    print(df)

    #salvar em csv
    df.to_csv('movies.csv', index=False)
    print('Tabela Salva com Sucesso!')

    print("Dados das datas extraídas", df['Data'].head())

    df['Data'] = pd.to_datetime(df['Data'], format='%d de %b de %Y', errors='coerce')
    print("Dados das datas extraídas", df['Data'].head())

    #garantir que as datas sejam corretamente interpretadas
    df['Data'] = pd.to_datetime(df['Data'], errors='coerce')

    #extraindo o mes e ano da data
    df['Mês/Ano'] = df['Data'].dt.to_period('M')

    #contagem de filmes por mes
    filmes_por_mes =  df['Mês/Ano'].value_counts().sort_index()

    #plotar o grafico de barras
    plt.figure(figsize=(10,6))
    filmes_por_mes.plot(kind='bar', color='green')
    plt.title('Quantidade de Filmes por Mês')
    plt.xlabel('Mês / Ano')
    plt.ylabel('Quantidade de Filmes')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


else:
    print("Nenhum dado encontrato")    



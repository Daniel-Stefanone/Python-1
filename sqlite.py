import sqlite3

#Abrir a conexão com o banco
conn = sqlite3.connect('meuBanco.db')
print("Conexão aberta!")

#Criar tabela no banco que está aberto
conn.execute('''
CREATE TABLE IF NOT EXISTS Alunos (
        matricula integer,
        nome string,
        curso string             
   );
''')
conn.commit()
print('Tabela criada com sucesso!!!')

#Inserir dados na tabela
conn.execute("INSERT INTO Alunos VALUES (1, 'Caio', 'Python');")
conn.execute("INSERT INTO Alunos VALUES (2, 'Eduardo', 'SQL');")
conn.execute("INSERT INTO Alunos VALUES (3, 'Mariana', 'Oracle');")
conn.execute("INSERT INTO Alunos VALUES (4, 'Vitor', 'NASA');")

conn.commit()
print('Dados inseridos com sucesso!!!')

#Consultar dados da tabela
alunos_encontrados = conn.execute('''
    SELECT matricula, nome FROM Alunos;
''')
for linhas in alunos_encontrados:
    print("Matricula" + str(linhas[0]))
    print("Nome" + str(linhas[1]))

import pandas as pd 
pedido = """ SELECT * FROM Alunos """

estruturadedados = pd.read_sql_query(pedido, conn)
estruturadedados

conn.close()






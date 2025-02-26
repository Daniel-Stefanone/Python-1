#Função para criar um carro com marca e modelo
def criar_carro(marca, modelo):
    return {"marca": marca, "modelo": modelo}

#Função para acelerar e parar o carro 
def acelerar(carro):
    print(f"O {carro['marca']} {carro ['modelo']} está acelerando.")  

def parar(carro):
    print(f"O {carro['marca']} {carro ['modelo']} parou.")         

#Função para cirar um carro com cor adicional
def criar_carro_com_cor(marca, modelo, cor):
    carro = criar_carro(modelo, marca)
    carro["cor"]= cor 
    return carro

#Exibir a cor do carro
def exibir_cor(carro):
    print(f"O carro é da cor {carro['cor']}.")

#Virar o carro para direita ou esquerda
def virar_para_direita(carro):
    print(f"O {carro['marca']} {carro ['modelo']} virou para direita.")         
def virar_para_esquerda(carro):
    print(f"O {carro['marca']} {carro ['modelo']} virou para esquerda.")  


#criando os carros
carro1 = criar_carro("Fuscal", "1984")
carro2 = criar_carro("Suzuki", "Jimmy")

#acelerando e parando os carros
print(carro1["marca"])   # acessando a marca
print(carro1["modelo"])  # acessando o modelo

#Criando o carro com cor
carro3 = criar_carro_com_cor("Toyota", "Ethios", "Branco")
print(carro3["marca"])
print(carro3["modelo"])
print(carro3["cor"])
exibir_cor(carro3)

print('----------Corrida----------')
acelerar(carro3)
parar(carro3)


print(carro2["marca"])
print(carro2["modelo"])
acelerar(carro2)
virar_para_direita(carro2)
virar_para_esquerda(carro2)
parar(carro2)







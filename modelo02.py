#Vamos comerçar criando uma classe chamada carro
#Uma classe é um molde ou planta que define como so objetos dessa classe serão 
#Ela define o que um objeto pode fazer (os métodos) e o que eles tem (os atributos)

class  Carro:
    #A classe carro tem dois atributos: "marca" e "modelo"; e um método: "acelerar".
    #O método especial __init__ é o que chama quando criamos um objeto da classe
    #Ele inicializa os atributos do objeto (marca e modelo)
    def __init__(self, marca, modelo, cor):
        #Os atributos do objeto serão definidos dentro do IndentationError# o self refere-se ao próprio objeto que está sendo criado
        self.modelo = modelo #atributo que armazena o modelo
        self.marca = marca   #atributo que armazena a marca
        self.cor = cor       #atribuindo cor ao carro   
    
    #Esse é o método que defini o comportamento do objeto, aqui estamos falando o que de fato o carro faz 
    def acelerar(self):
        print(f"O {self.marca} {self.modelo} está acelerando!")

    def parar(self):
        print(f"O {self.marca} {self.modelo} parou!")

    def direita(self):
        print(f"O {self.marca} {self.modelo} {self.cor} virou a direita!")

    def esquerda(self):
        print(f"O {self.marca} {self.modelo} {self.cor} virou a esquerda!")
    

carro1 = Carro("Fusca", "1984", "Preto")
print(carro1.marca)
print(carro1.modelo)
print(carro1.cor)
carro1.acelerar()
carro1.direita()
carro1.esquerda()
carro1.parar()
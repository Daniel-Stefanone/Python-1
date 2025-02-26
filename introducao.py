# isso é um comentário
''' a próxima linha mostra meu nome!'''
print("Daniel Stefanone")

print("Meu nome é: Daniel. \nMeu curso é: Python.")

""" 
Trabalhando com tipificação e variaveis
"""

nome = "Daniel" #string
sobrenome = "Stefanone"
idade = 40 #integer
altura = 1.71 #float
bermuda = False #boolean

print(nome + " " + sobrenome +" tem " + str(idade))

print(idade + 2)

textoVariasLinhas = '''
Operadores
Soma + 
Subtração - 
divisão / 
potencia ^
exponenciação ** 
multiplicação *
'''
print(textoVariasLinhas)

# Detalhamento das strings e usando formato
nomeCompleto = "Daniel Stefanone"
inicio = 5 
fim = inicio + 6
print(nomeCompleto[inicio:fim])


qNome = input("Insira seu nome :")
qSobrenome = input("Insira seu sobrenome :")
print("Seu Nome é:" + qNome + " " + qSobrenome)
from random import randint
from colorama import init, Fore

print("#### ---------- Vamos jogar? ---------- ####")

min = 0 
max = 100 
random = randint(min,max)
chute = 0 
chances = 10 

while chute != random:
    chute = input(f'Chute um número entre {min} a {max}\n')
    if chute.isnumeric():
        chute = int(chute)
        chances = chances - 1
        if chute == random:
            print('\o/ \o/ \o/ ')
            print('Parabéns você Venceu!!!! O Número era {} e você ainda tinha {} chances.'. format(random,chances))
            print('\o/ \o/ \o/ ')
            break
        else:
            print(' ')
            if chute > random: 
                print('Você Erroooouuuuuu! Dica: é um número menor!')
            else:
                print('Você Erroooouuuuuu! Dica: é um número maior!')
            print('Você ainda possui {} chances'. format (chances))
            print(' ')   
        if chances == 0:
           print(' ')       
           print('Suas chances acabaram você perdeu!')
           print(' ')  
           break

init(autoreset=True)
print(Fore.RED + "#### ---------- Game Over! ---------- ####")




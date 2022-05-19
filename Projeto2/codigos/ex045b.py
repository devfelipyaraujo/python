#Crie um algoritmo que faça o conputador jpgar JOKENPÔ com você.

from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')

print(' ')
computador = randint(0, 2)

print('''Suas Opções: \n
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')

print(' ')

jogador = int(input('Qual é a sua jogada? '))
print(' ')

print('JO')
sleep(1)

print('KEN')
sleep(1)

print('PO!!!!!')
sleep(1)

print(' ')

print('-='*11)
print('Computador jogou {}'.format(itens[computador]))

print(' ')
print('Jogador jogou {}'.format(itens[jogador]))
print('-='*11)

print(' ')

if computador == 0: #computador jogou PEDRA
    
    if jogador == 0:
        print('{}EMPATE!{}'.format('\033[35m', '\033[m'))

    elif jogador == 1:
        print('{}JOGADOR VENCEU!{}'.format('\033[32m', '\033[m'))

    elif jogador == 2:
        print('{}COMPUTADOR VENCEU!{}'.format('\033[31m', '\033[m'))
    
    else:
        print('{}JOGADA INVÁLIDA!{}'.format('\033[36m', '\033[m'))

elif computador == 1: #computador jogou TESOURA
   
    if jogador == 0:
        print('{}COMPUTADOR VENCEU!{}'.format('\033[31m', '\033[m'))

    elif jogador == 1:
        print('{}EMPATE!{}'.format('\033[35m', '\033[m'))

    elif jogador == 2:
        print('{}JOGADOR VENCEU!{}'.format('\033[32m', '\033[m'))
    
    else:
        print('{}JOGADA INVÁLIDA!{}'.format('\033[36m', '\033[m'))

elif computador == 2: #computador jogou PAPEL
    
    if jogador == 0:
        print('{}JOGADOR VENCEU!{}'.format('\033[32m', '\033[m'))

    elif jogador == 1:
        print('{}COMPUTADOR VENCEU!{}'.format('\033[31m', '\033[m'))

    elif jogador == 2:
        print('{}EMPATE!{}'.format('\033[35m', '\033[m'))
    
    else:
        print('{}JOGADA INVÁLIDA!{}'.format('\033[36m', '\033[m'))

else:
    print('fdsf')


print(' ')
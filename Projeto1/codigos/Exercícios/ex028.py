#Faça um algoritmo que faça o computador "pensar" em um número inteiro entre 0 e 5
#Faça o usuário tentardescobrir qual foi o número escolhido pelo compoutador. 

from random import randint
from time import sleep

computador = randint(0, 5) #faz o computador "PENSAR"
print('-=' * 28)
print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
print('-=' * 28)
jogador = int(input('Em que número eu pensei? ')) #jogador tenta adivinhar
print('PROCESSANDO...')
sleep(1)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}'.format(computador, jogador))

#Melhore o jogo do desafio 28 onde o computador vai pensar em um número entre 0 e 10;
#Só que agora o jogador vai tentar adivinhar até acertar;
#Mostrando no final quantos palpites foram necessários para vencer.

from random import randint
from time import sleep

tent = 0
computador = -1
jogador = None

print(' ')

while computador != jogador:
    
    computador = randint(0, 10) #faz o computador "PENSAR"

    jogador = int(input('Em que número eu pensei? ')) #jogador tenta adivinhar
    print(' ')

    tent += 1

    if jogador != computador:
        print('Não! Tente de novo')
        print(' ')
                
    else:
        print('PARABÉNS! Você conseguiu me vencer!')
        print(' ')

print('Foram necessárias {} tentativas para me vencer!'.format(tent))
print(' ')


from random import randint
from time import sleep

tent = 0
computador = randint(0, 10) #faz o computador "PENSAR"

print('-=' * 28)
print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
print('-=' * 28)

jogador = int(input('Em que número eu pensei? ')) #jogador tenta adivinhar

print('PROCESSANDO...')

sleep(1)

if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    while computador != jogador:
        
        computador = randint(0, 10) #faz o computador "PENSAR"

        jogador = int(input('Em que número eu pensei? ')) #jogador tenta adivinhar

        if jogador == computador:
            print('PARABÉNS! Você conseguiu me vencer!')
        
        else:
            tent += 1
            print('Não! Tente de novo')

print('Foram {} tentativas'.format(tent))
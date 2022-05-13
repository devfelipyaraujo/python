from random import randint
from time import sleep

computador = randint(0, 5) #faz o computador "PENSAR"
print('\033[32m-=\033[m' * 28)
#print('\033[33mVou pensar em um número\033[m entre 0 e 5. Tente adivinhar...')
print('\033[34mVou pensar em um número\033[m \033[40mentre 0 e 5. Tente advinhar...\033[m')
print('\033[33m-=\033[m' * 28)
jogador = int(input('\033[36mEm que número eu pensei?\033[m ')) #jogador tenta adivinhar
print('\033[31mPROCESSANDO...\033[m')
sleep(1)
if jogador == computador:
    print('\033[33;40mPARABÉNS!\033[m Você conseguiu me vencer!')
else:
    print('\033[31;40mGANHEI!\033[m Eu pensei no número \033[36m{}\033[m e não no \033[33m{}\033[m'.format(computador, jogador))

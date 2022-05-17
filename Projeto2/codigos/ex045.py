#Crie um algoritmo que faça o conputador jpgar JOKENPÔ com você.

import random
from time import sleep

pedra = 'pedra'
papel = 'papel'
tesoura = 'tesoura'

lista = [pedra, papel, tesoura]

computador = random.choice(lista)

print(' ')
jogador = input('Qual você escolhe?...\n \nPedra...\nPapel... \nTesoura...\n \n').strip().lower()
print(' ')

sleep(1)

print('JO-KEN-PÔ....')
print(' ')

if jogador == computador:
    print('Ora, ora.... Parece que empatamos...')
    print(' ')
    print('Eu escolhi {} e voce também escolheu {}.'.format(computador, jogador))
    print(' ')

elif jogador == pedra and computador == tesoura:
    print('AFF! Você ganhou essa. Na próxima tu nao terá sorte...')
    print(' ')
    print('Eu escolhi {} e voce escolheu {}.'.format(computador, jogador))
    print(' ')

elif jogador == pedra and computador == papel:
    print('HAHAHAHA! achou que pedra seria imbatível, né?...')
    print(' ')
    print('Eu escolhi {} e voce escolheu {}.'.format(computador, jogador))
    print(' ')

elif jogador == papel and computador == tesoura:
    print('CORTEI IGUAL CEROL FI........')
    print(' ')
    print('Eu escolhi {} e voce escolheu {}.'.format(computador, jogador))
    print(' ')

elif jogador == papel and computador == pedra:
    print('AFF! Você ganhou essa. Na próxima tu nao terá sorte...')
    print(' ')
    print('Eu escolhi {} e voce escolheu {}.'.format(computador, jogador))
    print(' ')

elif jogador == tesoura and computador == pedra:
    print('AMASSAAAAAAA, HAHAHAHHA...')
    print(' ')
    print('Eu escolhi {} e voce escolheu {}.'.format(computador, jogador))
    print(' ')

elif jogador == tesoura and computador == papel:
    print('AFF! Você ganhou essa. Na próxima tu nao terá sorte...')
    print(' ')
    print('Eu escolhi {} e voce escolheu {}.'.format(computador, jogador))
    print(' ')

else:
    print('Não entendi, vamos recomeçar...')
    print(' ')

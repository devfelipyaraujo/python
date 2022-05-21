#Melhore o jogo do desafio 28 onde o computador vai pensar em um número entre 0 e 10;
#Só que agora o jogador vai tentar adivinhar até acertar;
#Mostrando no final quantos palpites foram necessários para vencer.

from random import randint

print(' ')

computador = randint(0, 10) #faz o computador "PENSAR"

print('Olá, sou Jarvis! Acabei de pensar em um número....')
print('Consegue advinhar qual foi? ')


acertou = False
palpites = 0

while not acertou:
    print(' ')
    jogador = int(input('Qual o seu palpite? '))
   
    palpites += 1

    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('É mais que isso.. Tente de novo!')
            
        
        elif jogador > computador:
            print('É menos que isso.. Tente de novo!')
print(' ')
print('Acertou com {} tentativas. Parabéns!'.format(palpites))
print(' ')



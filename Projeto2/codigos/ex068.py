

from random import randint

#resp = ''
#P = ''
#I = ''
cont = 0
perdeu = False
print('Olá, sou Jarvis! Vamos jogar PAR ou ÍMPAR....')
print(' ')

while not perdeu:
    
    computador = randint(0, 100) #faz o computador "PENSAR"
    
    jogador = int(input('Diga  um valor: '))
    
    resp = str(input('PAR ou ÍMPAR [P/I] ')).strip().upper()[0]
    
    soma = computador + jogador

    if resp == 'I' and soma %2 == 0:
        print(28 * '--')
        print(f' Você jogou {jogador} e o computador {computador} resultado foi {soma} PAR')
        print(28 * '--')
        print('VOCÊ PERDEU!')
        perdeu = True
        print(' ')

    elif resp == 'P' and soma %2 == 0:
        print(28 * '--')
        print(f' Você jogou {jogador} e o computador {computador} resultado foi {soma} PAR')
        print(28 * '--')
        print(15 * '=-')
        print(' Você Venceu! VAMOS DE NOVO!')
        print(15 * '=-')
        cont += 1
        print(' ')
    
    elif resp == 'I' and soma %3 == 0:
        print(28 * '--')
        print(f' Você jogou {jogador} e o computador {computador} resultado foi {soma} ÍMPAR')
        print(28 * '--')
        print(15 * '=-')
        print(' Você Venceu! VAMOS DE NOVO!')
        print(15 * '=-')
        cont += 1
        print(' ')

    elif resp == 'P' and soma %3 == 0:
        print(28 * '--')
        print(f' Você jogou {jogador} e o computador {computador} resultado foi {soma} ÍMPAR')
        print(28 * '--')
        print('VOCÊ PERDEU!')
        perdeu = True
        print(' ')

if cont ==1:
    print(24 * '-=')
    print(f'GAME OVER!!! Você conseguiu me vencer {cont} vez!')
    print(24 * '-=')

else:
    print(24 * '-=')
    print(f'GAME OVER!!! Você conseguiu me vencer {cont} vezes!')
    print(24 * '-=')



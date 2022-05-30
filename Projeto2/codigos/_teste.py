#Faça um programa que jogue par ou ímpar com o computador;
#O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.



from random import randint

cont = 0

print(' ')
print('Olá, sou Jarvis! Vamos jogar PAR ou ÍMPAR....')
print(' ')

while True:
    
    jogador = int(input('Diga  um valor: '))

    computador = randint(0, 100) #faz o computador "PENSAR"

    resp = ' '

    while resp not in 'PI':
        resp = str(input('PAR ou ÍMPAR [P/I] ')).strip().upper()[0]
    
    soma = computador + jogador

    if resp == 'I' and soma %2 == 0:
        print(28 * '--')
        print(f' Você jogou {jogador} e o computador {computador} resultado foi {soma} PAR')
        print(28 * '--')
        print(' ')
        print('              VOCÊ PERDEU!')
        break
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
        print(' ')
        print('              VOCÊ PERDEU!')
        break

if cont ==1:
    print(' ')
    print(24 * '-=')
    print(f'GAME OVER!!! Você conseguiu me vencer {cont} vez!')
    print(24 * '-=')

elif cont == 0:
    print(' ')
    print(24 * '-=')
    print(f'GAME OVER!!! Você não me venceu nenhuma vez!')
    print(24 * '-=')

else:
    print(' ')
    print(24 * '-=')
    print(f'GAME OVER!!! Você conseguiu me vencer {cont} vezes!')
    print(24 * '-=')



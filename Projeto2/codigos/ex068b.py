

from random import randint

v = 0 #calula o número de vitórias consecutivas

while True:

    jogador = int(input('Digite um valor: '))
    computador = randint(0, 100)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    
    print(' ')

    print(f'Você Jogou {jogador} e o computador {computador}. Total de {total}', end=' ')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    
    print(' ')

    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    
    print('Vamos Jogar Novamente!!')
    print(' ')
print(f'GAME OVER! Você venceu {v} vezes seguidas')

            

#Faça um programa que mostre a tabuada de vários números um de cada vez, para cada valor digitado;
#O programa será interrompido quando o número solicitado for negativo.


while True:

    print(' ')
    num = int(input('Qual número deseja calcular a tabuada? '))
    print(' ')

    if num < 0:
        print('Você escolheu sair!')
        print('Esse software não calcula tabuada de números negativos. Obrigado!')
        break
        

    for c in range(1, 11):
        print('{} x {:2} = {:2}'.format(num, c, num*c))
    
    print(' ')

print(' ')
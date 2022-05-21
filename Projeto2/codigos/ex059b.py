#Escreva um algoritmo que leia dois valores e mostre o menu na tela com as opções;
#Somar, multiplicar, maior, novos números, sair do programa;
#Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep

print(' ')

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

opção = 0

while opção != 5:
    print(' ')
    print('''O QUE QUER FAZER? \n
    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NÚMEROS
    [ 5 ] SAIR DO PROGRAMA''')
    print(' ')

    opção = int(input('Qual é sua opção? '))
    print(' ')

    if opção == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é igual a {}'.format(n1, n2, soma))
    
    elif opção == 2:
        produto = n1 * n2
        print('A multiplicação entre {} e {} é igual a {}'.format(n1, n2, produto))
    
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))
    
    elif opção == 4:
        print('Informe os números novamente!')
        print(' ')
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
    
    elif opção == 5:
        print('Finalizando...')
    
    else:
        print('Opção inválida. Tente de novo!') 

print(' ')
sleep(2)
print('Fim do programa, Volte sempre!')
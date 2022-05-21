#Escreva um algoritmo que leia dois valores e mostre o menu na tela com as opções;
#Somar, multiplicar, maior, novos números, sair do programa;
#Seu programa deverá realizar a operação solicitada em cada caso.

opção = None

print(' ')
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

while opção != 4:
    
    

    print(' ')
    print('''O QUE QUER FAZER? \n
    [ 0 ] SOMAR
    [ 1 ] MULTIPLICAR
    [ 2 ] MAIOR
    [ 3 ] NOVOS NÚMEROS
    [ 4 ] SAIR DO PROGRAMA''')
    print(' ')

    opção = int(input('Sua opção: '))
    print(' ')

    if opção == 0:
        print('A soma dos valores {} e {} resulta em {}'.format(n1, n2, n1 + n2))

    elif opção == 1:
        print('A multiplicação dos valores {} e {} resulta em {}'.format(n1, n2, n1 * n2))

    elif opção == 2:

        if n1 > n2:
            print('Entre {} e {} o primeiro valor {} é o maior'.format(n1, n2, n1))

        elif n1 < n2:
            print('Entre {} e {} o segundo valor {} é o maior'.format(n1, n2, n2))
        
        else:
            print('Os valores informados são iguais')
    
    elif opção == 3:
        print('OK, vamos recomeçar!')
        print(' ')
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
    
    elif opção == 4:
        print('Finalizando....')
    
    else:
        print('Opção Inválida. Tente de novo.')
    
print(' ')
print('FIM')
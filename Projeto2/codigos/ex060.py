#Faça um algoritmo que leia um número qualquer e informe ao seu fatorial

from math import factorial

n = None

print(' ')

while n != 0:

    n = int(input('Digite um número interiro: '))
    
    if n <= -1:
        print('O número {} é negativo e fatorial de número negativo não existe'.format(n))

    else:
        num = factorial(n)

        print('O fatorial de {} é {}'.format(n, num))
    
    print(' ')

print(' ')
print('Fim do programa')
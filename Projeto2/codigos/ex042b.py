#Escreva um algoritmo que leia o comprimento de três retas;
#E diga se elas podem ou não formar um triângulo.
#Caso seja possível, mostre qula tipo de triângulo podem formar.

from time import sleep

print(' ')
print('ANALISADOR DE TRIÂNGULOS')
print(' ')
print(30*'{}-{}={}'.format('\033[31m', '\033[32m', '\033[m'))
print(' ')
sleep(1)

r1 = float(input('Insira o tamanho do primeiro seguimento: '))
print(' ')
sleep(1)

r2 = float(input('Insira o tamanho do segundo segmento: '))
print(' ')
sleep(1)

r3 = float(input('Insira o tamanho do terceiro segmento: '))
print(' ')
sleep(1)

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos a cima PODEM formar um triângulo', end=' ')

    if r1 == r2 == r3:
        print('{}EQUILÁTERO{}'.format('\033[31m', '\033[m'))
        
    elif r1 != r2 != r3 != r1:
        print('{}ESCALENO{}'.format('\033[31m', '\033[m'))
     
    else:
        print('{}ISÓSCELES{}'.format('\033[31m', '\033[m'))

else:
    print('Os seguimentos a cima {}NÃO PODEM{} formar um triângulo'.format('\033[31m', '\033[m'))

print(' ')

print(30*'{}-{}={}'.format('\033[31m', '\033[32m', '\033[m'))

print(' ')
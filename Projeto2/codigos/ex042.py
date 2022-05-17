#Escreva um algoritmo que leia o comprimento de três retas;
#E diga se elas podem ou não formar um triângulo.
#Caso seja possível, 

from time import sleep

print('ANALISADOR DE TRIÂNGULOS')
print('-='*30)
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

if r1 < r2 + r3 and r2 <r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos a cima PODEM formar um triângulo')
else:
    print('Os seguimentos a cima NÃO PODEM formar um triângulo')

if r1 == r2 == r3:
    print('equilatero')
elif r1 != r2 == r3 and r1 == r3 !=r2 and r3 == r2 != r1:
    print('Isósceles')



print('-='*30)
#Escreva um algoritmo que leia o comprimento de três retas;
#E diga se elas podem ou não formar um triângulo. Se

print('ANALISADOR DE TRIÂNGULOS')
print('-='*30)
r1 = float(input('Insira o tamanho do primeiro seguimento: '))
r2 = float(input('Insira o tamanho do segundo segmento: '))
r3 = float(input('Insira o tamanho do terceiro segmento: '))

if r1 < r2 + r3 and r2 <r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos a cima PODEM formar um triângulo')
else:
    print('Os seguimentos a cima NÃO PODEM formar um triângulo')

print('-='*30)

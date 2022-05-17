#Escreva um programa que leia dois números inteiros e compare-os;
#Mostre na tela quem é o maios dos dois ou se ambos sãp iguais.

print ('    ')

n1 = float(input('Digite o primeiro número: '))
print ('    ')

n2 = float(input('Digite o segundo número: '))
print ('    ')

if n1 > n2:
    print('O primeiro número é marior')
    
elif n1 < n2:
    print('O segundo número é maior')
    
else:
    print('não existe valor maior, os dois são iguais!')

print ('    ')
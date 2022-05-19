#Faça um algoritmo que leia o peso de cinco pessoas.
#Mostre qual foi o maior e o menor peso lidos. 


print(' ')

maior = 0
menor = 0

for p in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    
    else:
        if peso > maior:
            maior = peso
        
        if peso < menor:
            menor = peso
print(' ')

print('O maior peso lido foi de {} KG'.format(maior))
print(' ')
print('O menor peso lido foi de {} KG'.format(menor))
print(' ')


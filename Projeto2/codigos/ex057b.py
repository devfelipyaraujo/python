#Faça um programa que leia o sexo de uma pessoa, mas so aceite os valores 'M' ou 'F'
#Caso esteja errado, peça a digitação novamente ate ter um valor correto.


print(' ')
sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
print(' ')
while sexo not in 'MF':
    sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
print(' ')
print('Sexo {} resgistrado com sucesso'.format(sexo))
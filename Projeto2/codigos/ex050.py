#Escreva um algoritmo que leia seis números interiros;
#Mostre a soma apenas daqueles que forem pares;
#Se o valor digitado for ímpar desconsidere-o.

soma = 0
cont = 0

for c in range(1, 7):
    num = int(input('Digite um valor: '))

    if num %2 == 0:
        soma += num
        cont += 1

print(' ')

print('Voce informou {} números PARES e a soma foi {}'.format(cont, soma))
#Escreva um algoritmo que leia varios números até que o usuário digite 999 para sair;
#Depois de sair mostre quantos números foram digitados e a soma deles desconsiderando o 999

num = cont = soma = 0
num = int(input('Digite um número [999 PARA SAIR] '))

while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número [999 PARA SAIR] '))

print('Você digitou {} números e a entre eles foi {}'.format(cont, soma))
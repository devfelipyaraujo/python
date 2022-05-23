#Escreva um algoritmo que leia varios números até que o usuário digite 999 para sair;
#Depois de sair mostre quantos números foram digitados e a soma deles desconsiderando o 999. 


print(' ')

num = 0
soma = 0
cont = 0

while num != 999:
    
    num = int(input('Digite um número: [999 PAR ENCERRAR O PROGRAMA] '))

    cont +=1

    soma += num

    if num == 999:
        cont -= 1
        soma -= 999
        
        print(' ')
        print('Você escolheu sair...')
    
print(' ')

print('Voce informou {} números e a soma foi {}'.format(cont, soma))

print(' ')
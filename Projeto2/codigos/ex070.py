#Crie um programa que leia o nome e o preço de vários produtos. 
#O programa deverá perguntar se o usuário vai continuar ou não.
#No final, mostre: A) qual é o total gasto na compra. B) quantos produtos custam mais de R$1000. C) qual é o nome do produto mais barato.



print(' ')


cont = 0 #Conta quantos produtos foram comprados
contm = 0
soma = 0 #Soma o valor total gasto
valorprod = 0 #Calcula os produtos acima de 1000 reais
menor = 0 #Produto mais barato
barato = '' #Nome do produto mai barato

while True:

    nprod = str(input('Qual o nome do produto: '))
    vprod = float(input('Insira o valor do produto: R$ '))
    print(' ')

    cont +=1
    contm +=1
    soma += vprod

    if contm == 1:
        menor = vprod
    
    else:
        if vprod < menor:
            menor = vprod
            barato = nprod

    if vprod > 1000:
        valorprod += 1
    
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    print(' ')
        
    if resp == 'N':
        print('Finalizando Programa....')
        break

    


    print(' ')

print(f'Foram comprados {cont} produtos')
print(f'Ao todo {valorprod} produtos custaram mais de R$ 1.000,00 cada')
print(f'O total gasto na compra foi de R$ {soma:.2f}')
print(f'O produto mais brato foi {barato} que custa {menor:.2f}')

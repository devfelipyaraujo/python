#Crie um programa que leia vários números inteiros pelo teclado;
#No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos;
#O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

print(' ')

soma = 0
cont = 0
maior = 0
menor = 0
media = 0
r = 'S'

while r in 'Ss':

    print(' ')

    num = int(input('Digite um número: '))

    print(' ')

    soma += num
    cont +=1

    if cont == 1:
        maior == menor == num
    else:
        if num > maior:
            maior = num   
        if num < menor:
            menor = num

    r = str(input('Quer continuar? ')).upper().strip()[0]    

media = soma / cont        
print(' ')
print('voce digitou {} numeros e a média entre eles é {:.1f}'.format(cont, media))
print(' ')
print('O maior é número é {} e o menor é {}'.format(maior, menor))
print(' ')

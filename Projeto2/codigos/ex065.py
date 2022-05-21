




print(' ')

num = 0
soma = 0
cont = 0
maior = 0
menor = 0
r = '[S/N]'

while r != 'N':

    print(' ')

    num = int(input('Digite um número: '))

    print(' ')

    r = str(input('Quer continuar? ')).upper()

    cont +=1

    soma += num

    if num > maior:
            maior = num
        
    if num < menor:
            menor = num

print(' ')
print('voce digitou {} numeros e a média entre eles é {:.1f}'.format(cont, soma/cont))
print(' ')
print('O maior é número é {} e o menor é {}'.format(maior, menor))
print(' ')

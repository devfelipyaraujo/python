








num = 0
soma = 0
cont = 0

while num != 999:
    
    num = int(input('Digite um número: '))

    if num == 999:
        print('Você escolheu sair...')

    cont +=1

    soma += num

print(' ')

print('Voce informou {} números e a soma foi {}'.format(cont, soma - 999))
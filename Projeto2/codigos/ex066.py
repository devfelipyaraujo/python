
print('')
print('-' * 17, '\n [999 PARA SAIR]')
print('-' * 17)
soma = cont = 0

while True:
    num = int(input('Digite um número: '))
    print('')

    if num == 999:
        break
    
    soma += num
    cont += 1
print('-' * 52)
print(f' Foram digitados {cont} números e a soma entre eles é {soma}')
print('-' * 52)
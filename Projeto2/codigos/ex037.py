#Escreva um algoritmo que leia um número interiro e peça ao usuário para escolher a base de conversão
#1 - Para BINÁRIO 2 - Para OCTAL 3 - Para HEXADECIMAL

print(' ')

num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')

print(' ')
opção = int(input('Sua opção: '))
print(' ')

if opção == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))

elif opção == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))

elif opção == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))

else:
    print('Opção inválida. Tente novamente.')

print(' ')
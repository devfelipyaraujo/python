#Faça um algoritmo que leia um número interiro;
#Diga se ele é ou não um  número primo.

print(' ')

num = int(input('Digite um número: '))
tot = 0
print(' ')

for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    
    print('{}'.format(c), end=' ')

print(' ')

print('\n\033[mO número {} foi divisível {} vezes'.format(num, tot))
print(' ')

if tot == 2:
    print('E por isso ele É PRIMO')

else:
    print('E por isso ele NÃO É PRIMO')

print(' ')
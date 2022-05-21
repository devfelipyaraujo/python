#Faça um algoritmo que leia um número qualquer e informe ao seu fatorial

print(' ')

n = int(input('Digite um número para calcular seu fatorial: ')) #Numero a ser calculado
c = n #contador para fazer regreção
f = 1 #calculador fatorial

print('Calculando {}!'.format(n), end=' = ')

while c > 0:

    print('{}'.format(c), end='')

    print(' x ' if c > 1 else ' = ', end='')

    f *= c
    c -= 1

print('{}'.format(f))

print(' ')


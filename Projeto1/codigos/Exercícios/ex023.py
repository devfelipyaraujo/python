#Faça um algoritmo que leia um número entre 0 e 999
#Mostre na tela cada um dos dígitos separados

num = int(input('Informe o número: '))

# U = Unidade
# D = Dezena
# C = Centena
# M = Milhar

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('Analisnado o número {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))

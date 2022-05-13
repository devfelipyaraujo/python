#Escreva um algoritmo que leia um ano qualquer e mostre se ele é Bissexto.

'''a = int(input('Informe o ano: '))
b = 4
c = a % b
if c == 0:
    print('O ano {} é Bissexto'.format(a))
else:
    print('O ano {} não é Bissexto'.format(a))'''

from datetime import date
print('-=-'*20)
print('Digite 0 para analisar o ano atual')
ano = int(input('Informe o ano: '))
if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} não é BISSEXTO'.format(ano))
print('-=-'*20)
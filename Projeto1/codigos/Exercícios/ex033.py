#Faça um algoritmo que leia três números e mostre qual é o maior e qual é o menor.

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

#VERIFICANDO QUEM É O MAIOR
if n1 > n2 and n1 > n3:
    print('Entre os números informados o maior número é {}'.format(n1))
if n2 > n1 and n2 > n3:
    print('Entre os números informados o maior número é {}'.format(n2))
if n3 > n1 and n3 > n2:
    print('Entre os números informados o maior número é {}'.format(n3))

#VERIFICANDO QUEM É O MENOR
if n1 < n2 and n1 < n3:
    print('Entre os números informados o menor número é {}'.format(n1))
if n2 < n1 and n2 < n3:
    print('Entre os números informados o menor número é {}'.format(n2))
if n3 < n1 and n3 < n2:
    print('Entre os números informados o menor número é {}'.format(n3))

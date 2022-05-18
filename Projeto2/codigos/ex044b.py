

print(' ')
print(40*'{}*{}={}'.format('\033[36m', '\033[31m', '\033[m'))
print('{:^80}'.format('{}LORENZI VEST{}'.format('\033[36;1m', '\033[m')))
print(40*'{}*{}={}'.format('\033[36m', '\033[31m', '\033[m'))

preço = float(input('Preço das compras: R$ '))
print(' ')
print(''' FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro ou cheque
[ 2 ] à vista cartão de débito
[ 3 ] 2x no cartão
[ 4 ] 3x no ou mais no cartão''')

print(' ')
opção = int(input('Qual sua forma de pagamento? '))

if opção == 1:
    total = preço - (preço *10 /100)

elif opção == 2:
    total = preço - (preço *5 /100)

elif opção == 3:
    total = preço
    parcela = total /2
    print('Sua compra será parcelada em 2x de R$ {:.2f}'.format(parcela))

elif opção ==4:
    total = preço + (preço *10 /100)
    totparc = int(input('Quantas parcelas'))


print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final'.format(preço, total))

print(' ')
    
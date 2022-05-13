

#Crie um algoritmo que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
r = float(input('Quantos reais você tem na carteira? R$ '))
#cotação do dólar R$ 4,85
d = float(4.85)
c = float (r/d)
print('Com R$ {:.2f} é possivel realizar a compra de US$ {:.2f}'.format(r, c))

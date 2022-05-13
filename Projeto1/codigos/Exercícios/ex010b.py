

#Crie um algoritmo que leia quanto dinheiro uma pessoa tem na carteira
#Mostre quantas moedas estrangérias ela poderia comprar

r = float(input('Quanto dinheiro você tem na carteira? R$ '))
d = 4.77
e = 5.33
i = 0.04
l = 6.26
b = 225109.41
print ('-' *75)
print ('Na cotação atual com R$ {:.2f} é possível realizar a compra de US$ {:.2f}'.format(r, r/d))
print ('Na cotação atual com R$ {:.2f} é possível realizar a compra de   € {:.2f}'.format(r, r/e))
print ('Na cotação atual com R$ {:.2f} é possível realizar a compra de   ¥ {:.2f}'.format(r, r/i))
print ('Na cotação atual com R$ {:.2f} é possível realizar a compra de   £ {:.2f}'.format(r, r/l))
print ('Na cotação atual com R$ {:.2f} é possível realizar a compra de BTC {:.4f}'.format(r, r/b))

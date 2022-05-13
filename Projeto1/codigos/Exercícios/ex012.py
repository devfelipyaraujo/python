

#Crie um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.
p = float(input('Insira o valor do produto: R$ ' ))
d = ((p*5)/100)
t = (p-d)
print ('O produto que custava R$ {:.2f}, na promoção com o desconto de 5% vai custar R$ {:.2f}'.format(p, t))

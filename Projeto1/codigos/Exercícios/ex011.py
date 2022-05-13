
#Crie um algoritmo que leia a largura e altura de uma parede em metros.
#Calcule a sua área e a quantidade de tinta necessária para pintá-la.
#Sendo que cada litro de tinta pinta uma área de 2m²

l = float(input('Metros de largura: '))
a = float(input('Metros de altura: '))
t = float(l*a)
p = (t/2)
print('Sua parede tem a dimensão de {} x {} e sua área total são {} m²'.format(l, a, t))
print('Serão necessários {} litros de tinta para pintar todo esse espaço'.format(p))

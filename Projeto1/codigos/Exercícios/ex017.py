

#Faça um algoritmo que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo
#calcule e mostre o comprimento da hipotenusa. 

#-------------------------------- Método 1 - Sem importações ------------------------------------------------------#

#CO = cateto oposto
co = float(input('Informe o valor do cateto oposto:: '))

#CA = cateto adjacente
ca = float(input('Informe o valor do cateto adjacente: '))

#HI = Hipotenusa
hi = (ca ** 2 + co ** 2) ** (1/2)

print("O valor da hipotenusa é: {}".format(hi))


#-------------------------------- Método 2 - Importando biblioteca Math --------------------------------------------#

'''import math

#CO = cateto oposto
co = float(input('Informe o valor do cateto oposto: '))

#CA = cateto adjacente
ca = float(input('Informe o valor do cateto adjacente: '))

#HI = hipotenusa
pca = math.pow(ca, 2)
pco = math.pow(co, 2)
hi = pca + pco
r = math.sqrt(hi)

print ('O valor do cateto oposto e de {} e o cateto adjacente é de {}'.format(co, ca))
print ('Realizando os calculos baseado nas fórmulas de pitágoras o valor da hipotenusa é {}'.format(r))'''



#-------------------------------- Método 3 - Importando biblioteca Hypot -------------------------------------------#

from math import  hypot

#CO = Cateto Oposto
co = float(input('Informe o valor do cateto oposto: '))

#CA = Cateto Adjacente
ca = float(input('Informe o valor do cateto adjacent: '))

#HI = Hipotenusa
hi = hypot(co, ca)

print ('O valor da Hipotenusa é {:.2f}'.format(hi))
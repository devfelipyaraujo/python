#Faça um algoritmo que leia um ângulo qualquer
#Mostre o valor de seno, cosseno e tangente desse ângulo.

import math

angulo = float(input('Insira o valor do ângulo a ser calculado: '))
rad = math.radians(angulo)

print ('O ângulo {} tem o SENO {:.2f}'.format(angulo, math.sin(rad)))
print ('O ângulo {} tem o COSSENO {:.2f}'.format(angulo, math.cos(rad)))
print ('O ângulo {} tem a TANGENTE {:.2f}'.format(angulo, math.tan(rad)))


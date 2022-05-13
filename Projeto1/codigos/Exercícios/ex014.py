
#Escreva um algoritmo que leia uma temperatura em °C e a converta para °F.

tempc = float(input('Informe qual a temperatura em °C: '))
tempf = tempc * 1.8 + 32
print ('A temperatura de {} °C convertida é equivalente a {:.1f} °F'.format(tempc, tempf))


#Faça um algoritmo que calcule a sooma entre todos os números ímpares que são múltiplos de 3;
#E que se encontram no intervalo de 1 ate 500.


s = 0
cont = 0
for c in range(1, 501, 2):
    if c %3 == 0:
        cont = cont +1
        s = s + c

print('A soma de todos os {} valores solicitados é {}'.format(cont, s))
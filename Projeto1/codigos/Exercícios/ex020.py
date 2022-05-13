

#Faça um algoritmo que leia o nome de 4 alunos
#Faça o sorteio da ordem de apresentação de trabalhos

import random

a1 = input("aluno 1: ")
a2 = input("aluno 2: ")
a3 = input("aluno 3: ")
a4 = input("aluno 4: ")

ordem = [a1, a2, a3, a4]

print('A ordem de apresentação será {}'.format(random.sample(ordem, k=4)))
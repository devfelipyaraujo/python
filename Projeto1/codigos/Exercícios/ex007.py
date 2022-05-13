

#Crie um algoritmo que leia duas notas de um aluno, calcule e mostre a sua média.
aluno = input('Insira o nome do aluno: ')
n1 = float(input('Insira a nota 1: '))
n2 = float(input('Insira a nota 2: '))
m = ((n1 + n2) /2)
print('A média das notas do aluno {} é {}'.format(aluno, m))

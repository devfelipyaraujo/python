#crie um algoritmo para um professor sortear um de seus 4 alunos para apagar o quadro

import random

a1 = str(input('Insira o nome do primeiro aluno: '))
a2 = str(input('Insira o nome do segundo aluno: '))
a3 = str(input('Insira o nome do tercero aluno: '))
a4 = str(input('Insira o nome do quarto aluno: '))

aluno = [a1, a2, a3, a4]

print ('O aluno sorteado para apagar o quadro foi {}'.format(random.choice(aluno)))
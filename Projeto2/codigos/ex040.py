#Crie um programa que leia duas notas de um aluno e calcule a sua média;
#Mostre uma mensagem no final de acordo com a média atingida.

from time import sleep

cores = {'limpa':'\033[m', 
'branca':'\033[30m', 
'vermelho':'\033[31m', 
'verde':'\033[32m', 
'amarelo':'\033[33m', 
'azul':'\033[34m', 
'magenta':'\033[35m', 
'ciano':'\033[36m', 
'cinza':'\033[37m'}


aluno = str(input('Qual é o nome do aluno: '))
print(' ')
sleep(1)

n1 = float(input('Qual é a primeira nota? '))
print(' ')
sleep(1)

n2= float(input('Qual é a segunda nota? '))
print(' ')
sleep(1)

media = (n1 + n2) / 2
print(' ')
sleep(1)

print('A média desse aluno foi de {} - Por conta disso...'.format(media))
print(' ')
sleep(1)

if media < 50:
    print('O aluno {} está {}REPROVADO{}'.format(aluno, cores['vermelho'], cores['limpa']))
    print(' ')
    sleep(1)

elif media == 50 and media < 69:
    print('O aluno {} está de {}RECUPERAÇÃO{}'.format(aluno, cores['amarelo'], cores['limpa']))
    print(' ')
    sleep(1)
    
else:
    print('O aluno {} está {}APROVADO!{}'.format(aluno, cores['verde'], cores['limpa']))
    print(' ')
    sleep(1)


#Crie um algoritmo que leia o salário de um colaborador e mostre seu novo salário com 15% de aumento.
s = float(input('Insira o valor atual do seu salário: R$ '))
a = (s*15/100 +s)
print('O colaborador que ganha R$ {:.2f} de salário, com o aumento de 15% passará a ganhar R$ {:.2f}'.format(s, a))

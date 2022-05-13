#Escreva um algo que pergunte o valor do salário e calcule um auemnto;
#10% para salários superiores a R$1.250,00;
#15 % para os demais.

s = float(input('Qual o valor do seu saláio? '))
if s <= 1250:
    print('O valor do novo salário é de R$ {:.2f}'.format(s*15/100+s))
else:
    print('O valor do novo salário é de R$ {:.2f}'.format(s*10/100+s))

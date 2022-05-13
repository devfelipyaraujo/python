#Escreva um algoritmo para analisar crédito para financiamento de imóvel
#O algoritmo deve perguntar o valor da casa o salário do comprador e em quantos anos ele quer pagar
#Calcule o valor da prestação mensal sabendo que ela não pode exceder 30% da renda do comprador ou o financiamento será negado


v = float(input('Qual o valor da casa? R$ '))
s = float(input('Qual o valor do seu salário? R$ '))
a = float(input('Em quantos anos pretende pagar? '))

t = a *12
p = v / t
e = (s*30) /100

if e < p:
    print('Infelizmente o financiamento foi NEGADO!')
    print('Pois excede os 30% do valor da sua renda mensal')
else:
    print('a casa será paga em {:.0f} meses'.format(t))
    print('O valor da prestação será de R$ {:.2f}'.format(p))
   
#Escreva um algoritmo para analisar crédito para financiamento de imóvel
#O algoritmo deve perguntar o valor da casa o salário do comprador e em quantos anos ele quer pagar
#Calcule o valor da prestação mensal sabendo que ela não pode exceder 30% da renda do comprador ou o financiamento será negado


v = float(input('Qual o valor da casa? R$ ')) #valor da casa
s = float(input('Qual o valor do seu salário? R$ ')) #salario do comprador
a = float(input('Em quantos anos pretende pagar? ')) #tempo de financiamento

prestação = v / (a *12)
maximo = (s*30) /100

if maximo < prestação:
    print('Infelizmente o financiamento foi NEGADO!')
    print('Pois o valor da prestação excede os 30% do valor da sua renda mensal')
    print(' ')

else:
    print('a casa será paga em {:.0f} anos'.format(a))
    print('O valor da prestação será de R$ {:.2f}'.format(prestação))
    print(' ')
   
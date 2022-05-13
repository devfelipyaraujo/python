
#Escreva um algoritimo que leia a quantidade de dias de aluguel e quantos KM rodados teve um carro.
#Calcule o preço a pagar sabendo que, o aluguel custa R$60,00 por dia e R$0,15 por KM rodado.

dias = int(input('Informe quantos dias de alguel do veículo: '))
km = float(input('Informe quantos KM foram rodadaos com o veículo: '))
aluguel = dias * 60
kmr = km * 0.15
total = aluguel + kmr
print('O veículo foi alugado por {} dias e percorreu um total de {} KM'.format(dias, km))
print('O valor total a pagar é de R$ {:.2f}'.format(total))

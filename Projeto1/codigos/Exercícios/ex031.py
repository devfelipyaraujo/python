#Escreva um seleccion que leia a distancia de uma viagem em KM;
#Calcule o preço da passagem cobrando R$ 0,50 por KM para viagens ate 200KM;
#Calcule o preço da passagem cobrando R$ 0,45 por KM para viagens mais longas.

d = int(input('Qual a distancia em KM do seu destino? '))
if d <=200:
    print('o valor da sua viagem é de R$ {:.2f}'.format(d *0.50))
else:
    print('o valor da sua viagem é de R$ {:.2f}'.format(d * 0.45))

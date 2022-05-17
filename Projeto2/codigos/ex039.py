#Faça um programa que leia o ano de nascimento de um jovem;
#Informe de acordo com sua idade se ele ainda vai se alistar ao serviço militar;
#Se é hora de se alistar ou se já passou do tempo do alistamento;
#Mostrae o tempo que falta ou que passou do prazo.

from time import sleep
from datetime import date

print(' ')
nome = str(input('Qual o seu nome? '))
print(' ')
sleep(1)

nasc = int(input('Qual o ano do seu nascimento? '))
print(' ')
sleep(1)

print('Olá {} aguarde um momento enquanto estamos verificando suas informações...'.format(nome))
print(' ')
sleep(2)

ano = date.today().year
idade = ano - nasc
al = 18 #idade para alistamento
ia = idade - al
ia2 = al - idade

print('Estamos de volta....')
print(' ')
sleep(2)

if idade == 18:
    print('Você possui {} anos de idade, então deve se alistar esse ano.'.format(idade))
    
elif idade > 18 and idade == 19:
    print('Você possui {} anos de idade. Perdeu o prazo de alistamento. Deveria ter feito isso a {} ano atrás.'.format(idade, ia))
    
elif idade > 19:
    print('Você possui {} anos de idade. Perdeu o prazo de alistamento. Deveria ter feito isso a {} anos atrás.'.format(idade, ia))
    
elif idade < 18 and idade == 17:
    print('Você possui {} anos de idade. Está perto do período de alistamento que deverá ser feito daqui a {} ano.'.format(idade, ia2))
    
else:
    print('Você possui {} anos de idade. Ainda não está na hora de se alistar. Isso deverá ser feito daqui {} anos. '.format(idade, ia2))
    
print(' ')
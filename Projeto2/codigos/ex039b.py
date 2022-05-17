#Faça um programa que leia o ano de nascimento de um jovem;
#Informe de acordo com sua idade se ele ainda vai se alistar ao serviço militar;
#Se é hora de se alistar ou se já passou do tempo do alistamento;
#Mostrae o tempo que falta ou que passou do prazo.

from datetime import date

print(' ')
atual = date.today().year

nasc = int(input('Ano de nascimento: '))
print(' ')

idade = atual - nasc

print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
print(' ')

if idade == 18:
    print('Você precisa se alistar IMEDIATAMENTE!')

elif idade < 18:
    saldo = 18 - idade
    print('Aida faltam {} anos para o alistamento.'.format(saldo))
    print(' ')
    ano = atual + saldo
    print('Seu alistamento será em {}.'.format(ano))
    

elif idade > 18:
    saldo = idade -18
    print('Você já deveria ter se alistado a {} anos.'.format(saldo))
    print(' ')
    ano = atual - saldo
    print('Seu alistamento foi em {}.'.format(ano))

print(' ')

from datetime import date

print('')

ano = date.today().year
totmaior = 0
totmenor = 0

for c in range(1, 8):
    nasc = int(input('Digite o ano do seu nascimento: '))

    
    idade = ano - nasc
    
    if idade < 21:
        totmenor += 1
    else:
        totmaior += 1

print('')
print('Ao todo tivemos {} pessoas maiores de idade'.format(totmaior))
print('')
print('E tivemos {} pessoas menor de idade'.format(totmenor))
print('')

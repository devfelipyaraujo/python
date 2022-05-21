 #Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA
 #Mostrando os 10 primeiros termos da progressão usando a estrutura while

print('Gerador de PA')
print('-=' *10)
print(' ')

primeiro = int(input('Primeiro termo: '))
print(' ')
razão = int(input('Razão da PA: '))
print(' ')

termo = primeiro
cont = 1

while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += razão
    cont += 1

print('FIM')
print(' ')
print('-=' *10)
print(' ')
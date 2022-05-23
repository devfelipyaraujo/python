#Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos;
#O programa encerrará quando ele disser que quer mostrar 0 termos.

print(' ')
print('-=' *8)
print(' Gerador de PA')
print('-=' *8)
print(' ')

primeiro = int(input('Primeiro termo: '))
print(' ')
razão = int(input('Razão da PA: '))
print(' ')

termo = primeiro
cont = 1
total = 0
mais = 10

while mais != 0:

    total = total + mais

    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razão
        cont += 1

    print('Pausa')
    print(' ')

    mais = int(input('Quantos termos você quer mostrar a mais? '))
    
    print(' ')

print('-=' *22)
print(' Operação finalizada com {} termos mostrados'.format(total))
print('-=' *22)
print(' ')

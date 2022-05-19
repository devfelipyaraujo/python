
print(' ')

sexm = 0
sexf = 0

for p in range(1, 6):
    print('----- {}ª Pessoa -----'.format(p))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper()
    
    if sexo != 'M' and sexo != 'F':

        print('Sexo Inválido')
    


    print(' ')
print('A média de idade do grupo é de {} anos'.format((idade*idade))/5)

  
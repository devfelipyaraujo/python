
print(' ')

maioridadehomem = 0
nomevelho = ''
somaidade = 0
mediaidade = 0
totmulher20 = 0

for p in range(1, 5):
    print('----- {}ª Pessoa -----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()
    print(' ')
    somaidade += idade
    
    if p == 1 and sexo == 'M':
        maioridadehomem = idade
        nomevelho = nome
    
    if sexo == 'M' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    
    if sexo == 'F' and idade < 20:
        totmulher20 +=1    

mediaidade = somaidade /4

print(' ')
print('A média de idade do grupo é de {} anos'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))

  
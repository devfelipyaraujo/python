
pare = False
sexo = ''
contidade = 0
contsexo = 0
contmidade = 0

while not pare:
    
    print(10 * '-=' )
    print('CADASTRE UMA PESSOA')
    print(10 * '-=' )

    #while sexo not in 'MF':
        #sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
    
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()
    resp = str(input('Quer continuar? [S/N]: ')).upper().strip()
    
    if idade >= 18:
        contidade += 1
    
    if sexo == 'F' and idade < 20:
        contmidade += 1
    
    if sexo == 'M':
        contsexo += 1
    
    if resp == 'N':
        print('Obrigado!')
        break

print(' ')    
print(f'Temos {contidade} Pessoas maiores de idade')
print(f'Temos {contsexo} Homens cadastrados')
print(f'Temos {contmidade} Mulheres com menos de 20 anos.')
print(' ')   


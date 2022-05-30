#Crie um programa que leia a idade e o sexo de várias pessoas;
#A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar;
#No final, mostre: A) quantas pessoas tem mais de 18 anos. B) quantos homens foram cadastrados. C) quantas mulheres tem menos de 20 anos.


cont = 0 #conta o total de cadastrados
contidade = 0 #conta o total de pessoas maiores de idade
contsexo = 0 #conta quantos homens foram cadastrados
contmidade = 0 #conta quantas mulheres tem menos de 20 anos

while True:
        
    print(10 * '-=' )
    print('CADASTRE UMA PESSOA')
    print(10 * '-=' )

    idade = int(input('Idade: '))
    
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
        
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).upper().strip()

    cont +=1
    
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
print(f'Temos {cont} Pessoas cadastradas')
print(f'Temos {contidade} Pessoas maiores de idade')
print(f'Temos {contsexo} Homens cadastrados')
print(f'Temos {contmidade} Mulheres com menos de 20 anos.')
print(' ')   
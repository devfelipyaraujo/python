#Crie um algortimo que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas
#O nome com todas as letras minúsculas
#Quantas letras ao todo, sem considerar os espaços
#Quantas letras tem o primeiro nome

nome = str(input('Insira o nome: ')).strip()
sp = nome.split()
print('Seu nomé maiúsculo é {}'.format(nome.upper()))
print('Seu nomé minúsculo é {}'.format(nome.lower()))
print('Seu nome tem um total de {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome é {} e ele tem {} letras'.format(sp[0], len(sp[0])))
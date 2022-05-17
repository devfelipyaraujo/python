#Escreva um algoritmo para ler o peso e altura de uma pessoa e calcular o IMC;
#Após realizar o calculo mostre na tela o resultado e a categoria de peso desssa pessoa.


print(' ')
peso = float(input('Qual o seu peso? (Kg) '))
print(' ')

altura = float(input('Qual a sua altura? (m) '))
print(' ')

imc = peso / (altura **2)

print ('seu IMC é {:.1f}'.format(imc))
print(' ')

if imc <= 18.5:
    print('Você está {}ABAIXO DO PESO{}'.format('\033[33m', '\033[m'))
    
elif imc >= 18.6 and imc <= 25:
    print('Você está no seu {}PESO IDEAL{}'.format('\033[32m', '\033[m'))
    
elif imc > 25 and imc <= 30:
    print('Você está com {}SOBREPESO{}'.format('\033[33m', '\033[m'))
    
elif imc > 30 and imc <= 40:
    print('Você está com {}OBESIDADE{}'.format('\033[31m', '\033[m'))
    
elif imc > 40 and imc <= 50:
    print('Você está com {}OBESIDADE MÓRBIDA{}'.format('\033[31m', '\033[m'))
    
else:
    print('{}CHAMA O IBAMA, TEM UM ELEFANTE AQUIIIIIIIIIII!!!!!{}'.format('\033[31m', '\033[m'))

print(' ')
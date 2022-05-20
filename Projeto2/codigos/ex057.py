#Faça um programa que leia o sexo de uma pessoa, mas so aceite os valores 'M' ou 'F'
#Caso esteja errado, peça a digitação novamente ate ter um valor correto.


s = ''


while s != 'M' and s != 'F':

    s = str(input('Informe o Sexo: ')).upper()
    
    if s == 'F':
        print('Entendi! Você é do sexo Feminino	')
        f = 'Feminino'
        
    elif s == 'M':
        print('Entendi! Você é do sexo Masculino')
        m = 'Masculino'

    else:
         print('Não entendi! Por favor, responda novamente.')

print('FIM')
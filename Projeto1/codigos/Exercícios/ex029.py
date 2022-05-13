#Faça um algoritmo que leia a velocidade de um carro.
#Se ela ulgrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado
#A multa vai custar R$7,00 por cada km a cima do limite.

v = float(input('Qual era a velocidade do carro? '))
if v > 80:
    print('Você ultrapassou o limite de velocidade permitido, você será multado.')
    m = (v - 80) *7
    print('O valor da muta será R$ {:.2f}'.format(m))

print('Tenha um ótimo dia, dirija com segurança.')
#Escreva um algoritmo que calcula o valor a ser pago por um produto, considarando o seu preço normal a condição de pagamanto;
#A vista dinheiro ou cheque: 10% de desconto;
#A vista no cartão: 5% de desconto;
#Em ate 2x no cartão: preço normal;
#Em 3x ou mais no cartão: 20% de juros.

from time import sleep

print(' ')
produto = float(input('Qual é o preço do produto? '))
print(' ')
sleep(1)

pagamento = int(input('Qual tipo de pagamento? \n 1 - A vista dinheiro ou cheque \n 2 - A vista no cartão \n 3 - Em ate 2x no cartão \n 4 - Em 3x ou mais no cartão  '))
print(' ')
sleep(1)

if pagamento == 1:
    print('Identifiquei seu pagamento à vista, nesse caso te daremos um desconto de 10% sobre o valor total. ')
    print(' ')
    print('O valor do produto é R$ {:.2f} com nosso desconto aplicado você irá pagar R$ {:.2f}'.format(produto, produto - produto *10 /100))
    print(' ')

elif pagamento == 2:
    print('Identifiquei seu pagamento à vista com cartão, nesse caso te daremos um desconto de 5% sobre o valor total. ')
    print(' ')
    print('O valor do produto é R$ {:.2f} com nosso desconto aplicado você irá pagar R$ {:.2f}'.format(produto, produto - produto *5 /100))
    print(' ')

elif pagamento == 3:
    print('Identifiquei seu pagamento parcelado em 2x no cartão vista, nesse caso não será possível aplicar desconto.')
    print(' ')

elif pagamento == 4:
    print('Identifiquei seu pagamento foi parcelado em 3x ou mais, nesse caso terá um acrescimo de 20% sobre o valor total. ')
    print(' ')
    print('O valor do produto é R$ {:.2f} com o acrescimo aplicado você irá pagar R$ {:.2f}'.format(produto, produto + produto *20 /100))
    print(' ')

print('Obrigado pela preferencia, volte sempre!')
print(' ')

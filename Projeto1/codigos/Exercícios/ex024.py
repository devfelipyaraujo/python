#Faça um algoritmo que lei o nome de uma cidade e diga se ela começa  com o nome "SANTO"

cid = str(input('Em que cidade você nasceu? '))
print(cid[:5].upper() == 'SANTO')

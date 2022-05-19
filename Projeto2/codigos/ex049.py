#Refaça o Desafio 09, mostrando a tabuada de um número que o usuário escolher;
#So que agora utilizando um laço for. 


print(' ')
num = int(input('Digite um número para ver sua tabuada: '))
print(' ')

for c in range(1, 11):
    print('{} x {:2} = {}'.format(num, c, num*c))

print(' ')
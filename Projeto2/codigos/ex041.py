

from datetime import date
from time import sleep

print(' ')
nome = str(input('Qual o nome do atleta? ' ))
print(' ')
sleep(1)

idade = int(input('Qual o ano de nascimento do atleta? '))
print(' ')
sleep(1)

ano = date.today().year
id = ano - idade

if id <= 9:
    print('Por ter {} anos o atleta {} está na categoria MIRÍM'.format(id, nome))
    print(' ')
    sleep(1)

elif id > 9 and id <= 14:
    print('Por ter {} anos o atleta {} está na categoria INFANTIL'.format(id, nome))
    print(' ')
    sleep(1)

elif id > 14 and id <=19:
    print('Por ter {} anos o atleta {} está na categoria JUNIOR'.format(id, nome))
    print(' ')
    sleep(1)

elif id == 20:
    print('Por ter {} anos o atleta {} está na categoria SÊNIOR'.format(id, nome))
    print(' ')
    sleep(1)

else:
    print('Por ter {} anos o atleta {} está na categoria MASTER'.format(id, nome))
    print(' ')
    sleep(1)
    
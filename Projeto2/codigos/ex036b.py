from time import sleep
import emoji

cores = {'limpa':'\033[m', 
'branca':'\033[30m', 
'vermelho':'\033[31m', 
'verde':'\033[32m', 
'amarelo':'\033[33m', 
'azul':'\033[34m', 
'magenta':'\033[35m', 
'ciano':'\033[36m', 
'cinza':'\033[37m'}

print(' ')

print(emoji.emojize(20 *'{}:heavy_dollar_sign:{}'.format(cores['azul'], cores['limpa']), use_aliases=True))

print('{} OLÁ, SEJA MUITO BEM VINDO AO FINANCIA! {}'.format(cores['ciano'], cores['limpa']))

print(emoji.emojize(20 *'{}:heavy_dollar_sign:{}'.format(cores['azul'], cores['limpa']), use_aliases=True))

print(' ')

sleep(1)

v = float(input('{}Qual o valor do imóvel que deseja financiar? {}R$ '.format(cores['magenta'], cores['limpa'])))

if v >=500000:
    sleep(1)
    
    print(emoji.emojize(':dizzy_face: {} DIAXO!!! Essa mansão vai ser top, em?...{}'.format(cores['azul'], cores['limpa']), use_aliases=True))
    
    print(' ')
    
    sleep(1)

elif v >= 300000 and v < 500000:
    print(emoji.emojize(':scream: {} Eita!!! está querendo um baita imóvel em?...{}'.format(cores['azul'], cores['limpa']), use_aliases=True))
    
    print(' ')
    
    sleep(1)

elif v >= 150000 and v < 300000:
    print(emoji.emojize(':grinning: {} Com esse valor consegue negóciar um bom imóvel...{}'.format(cores['azul'], cores['limpa']), use_aliases=True))
   
    print(' ')
    
    sleep(1)

elif v >= 100000 and v < 150000:
    print(emoji.emojize(':grin: {} Vai conseguir um casinha confortável...{}'.format(cores['azul'], cores['limpa']), use_aliases=True))
   
    print(' ')
    
    sleep(1)

elif v >= 80000 and v < 100000:
    print(emoji.emojize(':sweat_smile: {} Um AP de solteiro bacana...{}'.format(cores['azul'], cores['limpa']), use_aliases=True))
    
    print(' ')

    sleep(1)

else:
    sleep(1)
    
    print(emoji.emojize(':cold_sweat: :pray: {} Que Deus te abençoe...{}'.format(cores['azul'], cores['limpa']), use_aliases=True))
    
    print(' ')

a = int(input('{}Em quantos anos pretende pagar? {}'.format(cores['magenta'], cores['limpa'])))

if a <= 5:
    sleep(1)

    print(emoji.emojize(':stuck_out_tongue: {} Hummm!!! Rico que fala, né?...{}'.format(cores['azul'], cores['limpa']), use_aliases=True))
    
    print(' ')

    sleep(1)

elif a > 5 and a <= 20:
    print(emoji.emojize(':satisfied: {} Filho de rico, certeza...{}'.format(cores['azul'], cores['limpa']), use_aliases=True))
    
    print(' ')
    
    sleep(1)

elif a > 20 and a <= 30:
    print(emoji.emojize(':relieved: {} Nem vai pensar no bolso...{}'.format(cores['azul'], cores['limpa']), use_aliases=True))
   
    print(' ')
    
    sleep(1)

elif a > 30 and a <= 45:
    print(emoji.emojize(':sunglasses: {} Desse jeito da para financiar ate 5 dessas...{}'.format(cores['azul'], cores['limpa']), use_aliases=True))
   
    print(' ')

    sleep(1)

else:
    print(emoji.emojize(':skull: {} ARREGO!! Quer deixar o banco no prejuízo, né?... :joy:{}'.format(cores['azul'], cores['limpa']), use_aliases=True))
    
    print(' ')

    sleep(1)

s = float(input('{}Qual o valor da sua renda mensal? {}R$ '.format(cores['magenta'], cores['limpa'])))

if (s*30)/100 >= v /(a*12)*90/100:
  
    sleep(1)
   
    print(emoji.emojize(':rage: {} Cria vergonha, com um salário desse deveria comprar a vista! {}'.format(cores['azul'], cores['limpa']), use_aliases=True))
   
    print(' ')
   
    sleep(1)

elif (s*30)/100 >= v /(a*12)*70/100 and (s*30)/100 < v /(a*12)*90/100:
    
    sleep(1)
    
    print(emoji.emojize(':sunglasses: {} Muito bem, vai ter facilidade em pagar...{}'.format(cores['azul'], cores['limpa']), use_aliases=True))
   
    print(' ')
    
    sleep(1)

elif (s*30)/100 >= v /(a*12)*50/100 and (s*30)/100 < v /(a*12)*70/100:
   
    sleep(1)
   
    print(emoji.emojize(':neutral_face: {} Vamos cruzar os dedos...{}'.format(cores['azul'], cores['limpa']), use_aliases=True))
  
    print(' ')
   
    sleep(1)

else:
    print(emoji.emojize(':disappointed_relieved: :pray: {} Espero que dê tudo certo...{}'.format(cores['azul'], cores['limpa']), use_aliases=True))
   
    print(' ')
    
    sleep(1)

t = a *12 #meses para pagamento
p = v / t #valor da mensalidade
e = (s*30) /100 #valor de 30% da renda

print(27 *'{}#-{}'.format(cores['ciano'], cores['limpa']))

print(emoji.emojize('{}Um instante, estamos analisando seus dados...{} :computer:'.format(cores['amarelo'], cores['limpa']), use_aliases=True))

sleep(2)

print(' ')

print(emoji.emojize('{}Verificando Score e protestos do {}SPC {}e{} SERASA...{} :stuck_out_tongue_closed_eyes: '.format(cores['amarelo'], cores['vermelho'],cores['amarelo'], cores['vermelho'], cores['limpa']), use_aliases=True))

sleep(2)

print(' ')

print(emoji.emojize('{}Consultando histórico de crédito...{} :money_with_wings:'.format(cores['amarelo'], cores['limpa']), use_aliases=True))

sleep(2)

print(' ')

print(emoji.emojize('{}Isso está demorando mais que o esperado... {}:sleeping: '.format(cores['amarelo'], cores['limpa']), use_aliases=True))

print(27 *'{}#-{}'.format(cores['ciano'], cores['limpa']))

print(' ')

sleep(2)

if e < p:
    print(emoji.emojize(33 *'{}:x:{}'.format(cores['vermelho'], cores['limpa']), use_aliases=True))
    
    print(emoji.emojize('{} Infelizmente o financiamento foi {}NEGADO!{} :sweat:'.format(cores['cinza'], cores['vermelho'], cores['limpa']), use_aliases=True))
    
    print(' ')
    
    sleep(1)
    
    print('{} Pois a mensalidade excede os {} 30% {}{} do valor da sua renda mensal{}'.format(cores['cinza'], '\033[37;41m', cores['limpa'], cores['cinza'], cores['limpa']))
    
    print(emoji.emojize(33 *'{}:x:{}'.format(cores['vermelho'], cores['limpa']), use_aliases=True))
    
    print(' ')
    
    sleep(2)
    
    print(52 *'{}#-{}'.format(cores['ciano'], cores['limpa']))
    
    print('{} VOCÊ PODE TENTAR REALIAZAR O PROCESSO EM UM PRAZO MAIOR DE PAGAMENTO OU UM IMÓVEL COM VALOR INFERIOR {}'.format('\033[37;41m', '\033[m'))
    
    print(52 *'{}#-{}'.format(cores['ciano'], cores['limpa']))
    
else:
    print(7 *'{}#-{}'.format(cores['ciano'], cores['limpa']))
    
    print(emoji.emojize('{}#'':exclamation:{}APROVADO{}:exclamation:''#{}'.format(cores['ciano'], cores['amarelo'], cores['ciano'], cores['limpa']), use_aliases=True))
    
    print(7 *'{}#-{}'.format(cores['ciano'], cores['limpa']))
    
    sleep(2)
    
    print(' ')
    
    print('{}Realizando calculos do valor de mensalidade...{}'.format(cores['verde'], cores['limpa']))
    
    sleep(2)
    
    print(' ')
    
    print('{}O imóvel deverá ser pago em até {} {:.0f} meses {} {}para que não haja aplicação de juros!'.format(cores['verde'], '\033[37;41m', t, cores['limpa'], cores['verde']))
    
    sleep(2)
    
    print(' ')
    
    print('{}O valor da prestação será de {} R$ {:.2f} {}'.format(cores['verde'], '\033[37;41m', p, '\033[m'))
    
    print(' ')

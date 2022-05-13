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
sleep(2)
v = float(input('{}Qual o valor do imóvel que deseja financiar? {}R$ '.format(cores['magenta'], cores['limpa'])))
s = float(input('{}Qual o valor da sua renda mensal? {}R$ '.format(cores['magenta'], cores['limpa'])))
a = float(input('{}Em quantos anos pretende pagar? {}'.format(cores['magenta'], cores['limpa'])))
print(' ')
t = a *12
p = v / t
e = (s*30) /100

print(25 *'{}#-{}'.format(cores['ciano'], cores['limpa']))
print(emoji.emojize('{}Um instante, estamos analisando seus dados...{} :computer:'.format(cores['amarelo'], cores['limpa']), use_aliases=True))
sleep(2)
print(' ')
print(emoji.emojize('{}Verificando Score e protestos do {}SPC {}e{} SERASA...{} :stuck_out_tongue_closed_eyes: '.format(cores['amarelo'], cores['vermelho'],cores['amarelo'], cores['vermelho'], cores['limpa']), use_aliases=True))
sleep(2)
print(' ')
print(emoji.emojize('{}Consultando histórico de crédito...{} :money_with_wings:'.format(cores['amarelo'], cores['limpa']), use_aliases=True))
sleep(2)
print(25 *'{}#-{}'.format(cores['ciano'], cores['limpa']))
print(' ')
if e < p:
    print(emoji.emojize(30 *'{}:x:{}'.format(cores['vermelho'], cores['limpa']), use_aliases=True))
    print(emoji.emojize('{} Infelizmente o financiamento foi {}NEGADO!{} :sweat:'.format(cores['cinza'], cores['vermelho'], cores['limpa']), use_aliases=True))
    print(' ')
    print('{} Pois a mensalidade excede os {} 30% {}{} do valor da sua renda mensal{}'.format(cores['cinza'], '\033[37;41m', cores['limpa'], cores['cinza'], cores['limpa']))
    print(emoji.emojize(30 *'{}:x:{}'.format(cores['vermelho'], cores['limpa']), use_aliases=True))
    print(' ')
    print(52 *'{}#-{}'.format(cores['ciano'], cores['limpa']))
    print('{} VOCÊ PODE TENTAR REALIAZAR O PROCESSO EM UM PRAZO MAIOR DE PAGAMENTO OU UM IMÓVEL COM VALOR INFERIOR {}'.format('\033[37;41m', '\033[m'))
    print(52 *'{}#-{}'.format(cores['ciano'], cores['limpa']))
else:
    print('{}Realizando calculos do valor de mensalidade...{}'.format(cores['verde'], cores['limpa']))
    sleep(2)
    print(' ')
    print('{}O imóvel deverá ser pago em até {} {:.0f} meses {} para que não haja aplicação de juros!'.format(cores['verde'], '\033[37;41m', t, cores['limpa'], cores['verde']))
    sleep(2)
    print(' ')
    print('{}O valor da prestação será de {} R$ {:.2f} {}'.format(cores['verde'], '\033[37;41m', p, cores['limpa']))
    #print('O valor da prestação deve ser no máximo R$ {:.2f}'.format(e))

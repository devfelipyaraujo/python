
#Códigos de Estilo
''' 0 = nada 
    1 = Negrito
    4 = Sublinhado
    7 = inverte as cores de fundo e texto'''

#Códigos de Cores
''' 30 = branco
    31 = vermelho
    32 = verde
    33 = amarelo
    34 = azul 
    35 = magenta
    36 = ciano
    37 = cinza '''

#Códigos de Fundo do texto
''' 40 = branco
    41 = vermelho
    42 = verde
    43 = amarelo
    44 = azul 
    45 = magenta
    46 = ciano
    47 = cinza'''

#Código padrão
   '\033[  m'
#Entre o '[' e o 'm' deve inserir o código do estilo;cor;fundo

#Estrutura para importar cores

cores = {'limpa':'\033[m', 
'branca':'\033[30m', 
'vermelho':'\033[31m', 
'verde':'\033[32m', 
'amarelo':'\033[33m', 
'azul':'\033[34m', 
'magenta':'\033[35m', 
'ciano':'\033[36m', 
'cinza':'\033[37m'}

#Método de importação

print('Teste de cores importadas')
print('{} Azul {} Vermelho {} Verde'.format(cores['azul'], cores['vermelho'], cores['verde'],))
print('{} Amarelo {} Branco {} Magenta'.format(cores['amarelo'], cores['branca'], cores['magenta']))
print('{} Ciano {} Cinza {} Limpa'.format(cores['ciano'], cores['cinza'], cores['limpa']))
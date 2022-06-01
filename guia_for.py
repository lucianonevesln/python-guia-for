# Guia for em Python

# Conteudo extraido da documentacao oficial e acrescido de observacoes
# e variacoes pessoais.

# Nota: nao e um guia definitivo, ha muitas outras possibilidades de
# iteracao que com certeza estao fora desse artigo.

# A declaracao for em Python e diferente de quando e usada em
# em C ou Paschal. Em vez de sempre iterar sobre uma progressao
# aritmetica de numeros (como em Paschal), ou dando ao usuario
# habilidade para definir ambas iteracao condicional degrau
# e parando (como em C), a declaracao de for do Python ocorre
# sobre o item de uma sequencia (lista ou string), em ordem e elas
# aparecem na sequencia.

# Os exemplos abaixo sao aplicaveis a uma lista e uma lista de
# dicionarios.

# lista de nomes
nomes = ['Nome_1', 'Nome_2', 'Nome_3', 'Nome_4']

print('\n----------------------------------------\n')

print('for que percorre uma lista por indice\n')
for indice in range(len(nomes)):
    print('Indice de nomes -> ', indice)

print('\n----------------------------------------\n')

print('for que percorre por cada item da lista\n')
for nome in nomes:
    print('Nome na lista -> ', nome)

print('\n----------------------------------------\n')

print('for que mostra a quantidade de letras por item\n')
for nome in nomes:
    print('Nome -> ', nome, '| Quantidade de caracteres -> ', len(nomes))

print('\n----------------------------------------\n')

# dicionario de usuarios
usuarios = [
    {
        'nome': 'Nome_1',
        'sobrenome': 'Sobrenome_1',
        'idade': 40
    },
    {
        'nome': 'Nome_2',
        'sobrenome': 'Sobrenome_2',
        'idade': 30
    },
    {
        'nome': 'Nome_3',
        'sobrenome': 'Sobrenome_3',
        'idade': 20
    },
    {
        'nome': 'Nome_4',
        'sobrenome': 'Sobrenome_4',
        'idade': 10
    },
]

print('for que mostra cada conjunto de elementos da lista\n')
for usuario in usuarios:
    print('Usuario: forma 1 -> ', usuario)

print('\n----------------------------------------\n')

print('variacao de for que mostra cada conjunto de elementos da lista\n')
for usuario in usuarios:
    print('Usuario: forma 1 -> ', usuario.items())

print('\n----------------------------------------\n')

print('for que percorre o dicionario por indice\n')
for indice in range(len(usuarios)):
    print('Indice de usuario -> ', indice)

print('\n----------------------------------------\n')

print('for que apresenta todas as chaves de um dicionario\n')
for usuario in usuarios:
     for chave in usuario:
         print('Nome da chave: forma 1 ->', chave)

print('\n----------------------------------------\n')

print('variacao de for que apresenta todas as chaves de um dicionario\n')
for usuario in usuarios:
    for chave in usuario.keys():
        print('Nome da chave: forma 2 ->', chave)

print('\n----------------------------------------\n')

print('for que mostra o valor associado a cada chave de um dicionario\n')
for usuario in usuarios:
    for valor_chave in usuario:
        print('Valor associado a chave: forma 1 -> ', usuario[valor_chave])

print('\n----------------------------------------\n')

print('variacao de for que mostra o valor associado a cada chave de um dicionario\n')
for usuario in usuarios:
    for valor_chave in usuario.values():
        print('Valor associado a chave: forma 2 -> ', valor_chave)

print('\n----------------------------------------\n')
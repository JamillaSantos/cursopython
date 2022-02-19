"""
Operadores Lógicos
23. Operadores lógicos + IFELIFELSE
and, or, not, in e not in
"""

# And Realiza duas comparações. As duas precisam ser verdadeiras
# Verdadeiro E Verdadeiro = True
# comparacao1 and comparacao2

# Verdadeiro E Falso = False
# comparacao1 and comparacao2


# Or Realiza duas comparações. Uma ou outra precisa ser verdadeira
# Verdadeiro OU Verdadeiro = True
# comparacao1 or comparacao2

# Verdadeiro OU Falso = True
# comparacao1 or comparacao2

# Falso OU Verdadeiro = True
# comparacao1 or comparacao2


# Not Não compara duas sentenças. É considerado um Inversor
# Exemplo
a = 2
b = 3

if b > a:
    print('B é maior do que A.')
else:
    print('A é maior do que B.')

# Invertendo (usando o NOT)
a = 2
b = 3

if not b > a:
    print('B é maior do que A.')
else:
    print('A é maior do que B.')

# Usado para verificar campo vazio/zerado
a = ''
b = 0

if not a:
    print('Preencha o valor de A.')
if not b:
    print('Preencha o valor de B.')

# In
nome = 'Jamilla da Hora'

if 'Hora' in nome:
    print('Existe HORA no seu nome')
else:
    print('Não existe.')

# Not in - Inverte a expressão anterior
nome = 'Jamilla da Hora'

if 'U' not in nome:
    print('Não existe U no seu nome')
else:
    print('Existe.')
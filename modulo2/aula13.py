"""
25. len - Quantidade de caracteres
não funciona com tipos numéricos e booleano
"""

'''
usuario = input('Digite seu usuário: ')
qtd_caracteres = len(usuario)

print(usuario, qtd_caracteres, type(qtd_caracteres))

if qtd_caracteres < 6:
    print('Você precisa digitar pelo menos 6 caracteres.')
else:
    print('Usuário cadastrado!')
'''

string1 = input('Digite alguma coisa: ')
string2 = input('Digite outra coisa: ')

print(f'A qtd total de caracteres digitados foi {len(string1) + len(string2)}')

print(len(string2))
print(string2.__len__())
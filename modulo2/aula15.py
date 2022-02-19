"""
27. Pass e Ellipsis como placeholders - reservar um lugar no código para escrever posteriormente
"""

valor = True

'''
if valor:
    print('Oi')
else:
    print('Tchau')
'''

# Erro de sintaxe pois o interpretador espera uma ação
'''
if valor:
    #Comentário
else:
    print('Tchau')
'''

# Tratando com o pass - o interpretador "pula" pra próxima linha de código
'''
if valor:
    pass
else:
    print('Tchau')
'''

# Tratando com Ellipsis - faz a mesma coisa do pass
if valor:
    ...
else:
    print('Tchau')

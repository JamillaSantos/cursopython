"""
Condições IF, ELIF e ELSE
20. IF, ELIF e ELSE + Booleans
"""

'''
if True:
    print("Verdadeiro")

    num_1 = 2
    num_2 = 4

    print(num_1 + num_2)
'''

'''
if False:
    print("Verdadeiro")
print("A minha expressão não é verdadeira")
'''

'''
if False:
    print("Verdadeiro")
else:
    print("Não é verdadeira")
'''
'''
if False:
    print("Verdadeiro")
elif True:
    print("Agora é verdadeiro")
else:
    print("Não é verdadeira")
'''

'''
if False:
    print("Verdadeiro")
elif True:
    print("Agora é verdadeiro")  #Executado o primeiro true e ignorada o resto
elif True:
    print("Mais uma verdadeira")
else:
    print("Não é verdadeira")
'''

'''
if False:
    print("Verdadeiro")
elif False:
    print("Agora é verdadeiro")  
elif False:
    print("Mais uma verdadeira")
else:
    print("Não é verdadeira")  #Else só é executado se nada antes for verdadeiro
'''

'''
if False:
    print("Verdadeiro")
elif False:
    print("Agora é verdadeiro")  #Se tudo for falso e não houver um else, nada será executado
elif False:
    print("Mais uma verdadeira")
'''

if True:
    print("Verdadeiro")
    print("teste teste2")
elif False:
    print("Agora é verdadeiro")  #Todo o bloco de código dentro da hierarquia será executado
    nome = input("Qual o seu nome? ")

    print(f'Seu nome é: {nome}.')
elif False:
    print("Mais uma verdadeira")
    print( 22 + 22 )
else:
    print("Não é verdadeira")
    print("blablabla")

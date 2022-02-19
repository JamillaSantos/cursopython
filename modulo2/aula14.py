"""
26. Documentação e funções built-in úteis
"""

num1 = input('Digite um número: ')
num2 = input('Digite outro número: ')

#num1 = int(num1)
#num2 = int(num2)

#print(num1 + num2)

# Funções de string -> isnumeric isdigit isdecimal: checam se a string pode ser convertida em inteiro

#print(num1.isnumeric())  # checa se tem números e positivos e não flutuantes
#print(num2.isnumeric())

'''Essa solução não consegue somar, por exemplo, números flutuantes'''

if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)

    print(num1 + num2)
else:
    print('Informe somente valores numéricos.')
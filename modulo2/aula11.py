"""
Operadores Relacionais
== > >= < <= !=
Retorna valor boolean
21. Operadores relacionais + IFELIFELSE
"""

# == Igualdade
print(2 == 2)
print(2 == 1)
print(2 == '2')

num1 = 2
num2 = 2
expressao = (num1 == num2)
print(expressao)


# >= Maior que ou igual a
num1 = 2
num2 = 2
num3 = 3
expressao = (num1 >= num2)
#expressao = (num3 > num1)
print(expressao)

# > Maior que
num1 = 2
num2 = 2
num3 = 3
#expressao = (num1 > num2)
expressao = (num3 > num1)
print(expressao)

# < Menor que
num1 = 2
num2 = 2
num3 = 3
#expressao = (num1 < num2)
expressao = (num1 < num3)
print(expressao)

# <= Menor que ou igual a
num1 = 2
num2 = 2
num3 = 3
expressao = (num1 <= num2)
#expressao = (num3 <= num1)
print(expressao)

# != Diferente
var1 = 'letra'
var2 = 'numero'

expressao = (var1 != var2)

print(expressao)

'''
# Exemplo Empréstimo

nome = input('Qual o seu nome? ')
idade = input('Qual a sua idade? ')

idade_limit = 18
idade = int(idade)

if idade >= idade_limit:
    print(f'{nome}, seu empréstimo foi liberado!')
else:
    print(f'Não foi dessa vez, {nome}. Idade não permitida :(.')

'''

# Exemplo Empréstimo 2

nome = input('Qual o seu nome? ')
idade = input('Qual a sua idade? ')

idade_limit = 20
idade_limit2 = 30

idade = int(idade)

if idade >= idade_limit and idade <= idade_limit2:
    print(f'{nome}, seu empréstimo foi liberado!')
else:
    print(f'Não foi dessa vez, {nome}. Idade não permitida :(.')



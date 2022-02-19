
"""
Tipos de dados
str - string - "Assim" | 'Assim'
int - inteiro - 123456 | -10 | 20
float - real/ponto flutuante - 1.0 | 10.50 | -50.93
bool - booleano/lógico - true/false
"""

# print(type('Luiz'))
print('Luiz', type('Luiz'))
print(1234, type(1234))
print(12.34, type(12.34))
print(10 == 10, type(10 == 10))

"""
Resultado:
Luiz <class 'str'>
1234 <class 'int'>
12.34 <class 'float'>
True <class 'bool'>
"""

# Type Casting (convertendo tipo de dado)

print('luiz', type('luiz'), bool('luiz'))
print('10', type('10'), type(int('10')))

# Exercício

# string: Nome
print('Jamilla da Hora', type('Jamilla da Hora'))

# int: Idade
print(37, type(37))

# float: Altura
print(1.70, type(1.70))

# bool: Eh maior de idade?
print(37 > 18, type(37 > 18))

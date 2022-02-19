"""
Operadores aritméticos
+ - Adição
- - Subtração
* - Multiplicação
/ - Divisão
// - Divisão inteira (resultado arredondado)
** - Exponenciação (eleva um número a outro)
% - Resto da divisão
() - Utilizado pra alterar a precedência
"""

print('Adição +', 10 + 10)
print('Subtração -', 10 - 5)
print('Multiplicação *', 10 * 10)
print('Divisão /', 10 / 5)
print('Divisão Inteira //', 10 // 3)
print('Pontenciação **', 2 ** 10)
print('Módulo %', 10 % 3)  # Traz o resta da divisão

# Precedência ()
print(5 + 2 * 10)
print((5 + 2) * 10)

# O * pode servir como operador de repetição
print(10 * '10')

# O + pode servir pra concatenar strings
print('5' + '5')
print('Jamilla', 'da', 'Hora e ela tem', str(37), 'anos')  # Type Casting (convertendo tipo de dado)

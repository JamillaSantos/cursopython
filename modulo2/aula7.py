"""
Introdução à formatação de Strings
"""

nome = 'Jamilla'
idade = 37
altura = 1.70
e_maior = idade > 18
peso = 69
imc = (peso/altura**2)

print(nome, 'tem', idade, 'de idade e seu IMC é', imc)
print(f'{nome} tem {idade} anos de idade e seu IMC é {imc:.2f}')
print('{} tem {} anos de idade e seu IMC é {:.2f}'.format(nome, idade, imc))
print('{0} tem {1} anos de idade e seu IMC é {2:.2f}'.format(nome, idade, imc))
print('{2} {0} {0} tem {1} anos de idade e seu IMC é {2:.2f}'.format(nome, idade, imc))
print('{i} tem {n} anos de idade e seu IMC é {im:.2f}'.format(n=nome, i=idade, im=imc))


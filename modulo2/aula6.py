"""
Variáveis - Iniciar com letra, pode conter números, separar _, letras minúsculas
"""
#nome = 'Jamilla' #Salva valor na memória do computador
#print(nome, type(nome))

nome = 'Jamilla'
idade = 37
altura = 1.70
e_maior = idade > 18
peso = 69
data_atual = 2022
data_1 = True
imc = (peso/altura**2)  # O operador ** já possui maior precedência

print('Nome:', nome, type(nome))
print('Idade:', idade, type(idade))
print('Altura:', altura, type(altura))
print('É maior?', e_maior, type(e_maior))

print(idade * altura)

# Exercício - Calcular o IMC

print(nome, 'tem', idade, 'de idade e seu IMC é', imc)

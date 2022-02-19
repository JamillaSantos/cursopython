"""
* Criar variáveis para nome (str), idade (int),
* altura (float) e peso (float) de uma pessoa
* Criar variável com o ano atual (int)
* Obter o ano de nascimento da pessoa (baseado na idade e ano atual)
* Obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
* Exibir um texto com todos os valores na tela usando F-Strings (com chaves)

* Ex.:
* Fulano tem XX anos, XX de altura e pesa XXkg.
* O IMC de Fulano é XX.
* Fulano nasceu em XXXX.
"""

nome = 'Jamilla da Hora'
idade = 37
altura = 1.72
peso = 69.0
ano_atual = 2022
ano_nasc = ano_atual - idade
imc = peso / altura**2

print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso}Kg.')
print(f'O IMC de {nome} é {imc:.2f}.')
print(f'{nome} nasceu em {ano_nasc}.')


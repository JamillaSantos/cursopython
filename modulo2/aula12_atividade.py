"""
Validação de usuário e senha
"""

usuario = input("Usuário: ")
senha = input("Senha: ")

usuario_bd = 'jamilla'
senha_bd = '123456'

if usuario_bd == usuario and senha_bd == senha:
    print('Usuário logado no sistema!')
else:
    print('Verifique o usuário e/ou senha!')

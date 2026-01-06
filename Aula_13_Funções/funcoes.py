# Funções

# Funções são blocos de código reutilizáveis que realizam
# uma tarefa específicca. Em vez de escrever o mesmo código
# várias vezes, criamos uma função e apenas a chamamos sempre que necessaário.

# Exemplo "real"
# Imagine que você tem que calcular o imposto de vários produtos em uma loja.
# Em vez de repetir a mesma conta várias vezes, vovê pode criar uma função
# chamada calcular_imposto() e usá-la sempre que precisar.

def saudacao(nome):
    print(f"Olá, {nome}! Bem-vindo ao curso de Python.")

nome = input("Digite seu nome: ")
saudacao(nome)
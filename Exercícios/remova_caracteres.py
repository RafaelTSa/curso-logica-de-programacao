def remove_char(nome):
    return nome[1:-1]

print("Digite seu nome: ")
nome = input(">>> ")

resultado = remove_char(nome)

print(f"Seu nome sem a primeira e a última letra: {resultado}")
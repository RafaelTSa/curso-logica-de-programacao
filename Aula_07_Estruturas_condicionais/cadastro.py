# cadastro com login e senha
# usuario digita nome, nascimento, e senha para efetuar login
ano_atual = 2025

print("-" *20)
print("Seja bem vindo!")
print("-" *20)
cadastro = input("ja é cadastrado no nosso site? (S/N)")
if cadastro == "N" or cadastro =="n":
    usuario = input("Digite seu nome de usuário:")
    data_nascimento = int(input("Digite o ano em que nasceu:"))
    idade = (ano_atual - data_nascimento )
    senha1 = int(input("Digite sua senha: "))
    senha2 = int(input("Digite sua senha novamente: "))
    if senha1 == senha2:
        print("-" *38)
        print(f"Parabéns {usuario} cadastro concluido.")
        print("-" *38)
    else:
        print("-" *38)
        print("senhas diferentes, volte do inicio.")
        print("-" *38)
else:
    print("-" *20)
    print("Bem vindo de volta")
    print("-" *20)
    usuario = input("Digite seu nome:")
    senha = int(input("Digite a senha:"))

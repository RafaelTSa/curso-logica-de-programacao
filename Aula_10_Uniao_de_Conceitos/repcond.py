# Juntando conceitos juntando laços de repetições e condicionais.

# Todas as estruturas podem ser usadas separadamente, mas
# em um programa "real", vamos undindo todas essas estruturas
# para criarmos os cenários que precisamos para resolver um problema!

# Exemplo:

# Você quer saber se um apalavra contém a letra Y

palavra = "Python"
letra_procurada = "y"

for letra in palavra:
    if letra == letra_procurada:
        print("Essa palavra tem a letra Y!")

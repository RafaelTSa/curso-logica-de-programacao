# Jogo de adivinhação

# No jogo, o usuário precisa adivinhar um número secreto.
# Ele pode tentar várias vezes até acertar.

numero_secreto = 6
tentativa = 0

while tentativa != numero_secreto:
    tentativa = int(input("Tente adivinhar um número de 1 a 10: "))
    if tentativa < numero_secreto:
        print("O número secreto é maior que", tentativa)
    elif tentativa > numero_secreto:
        print("O número secreto é menor que", tentativa)
else:
    print("Parabéns! Você acertou!")
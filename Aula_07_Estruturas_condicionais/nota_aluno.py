# Verificando a nota de um aluno

nota = float(input("Digite sua nota: "))  #Usúario insere a nota

if nota >= 7:
    print("Parabéns! Você passou de ano!")
elif nota >= 5:
    print("Você está de recuperação. Estude mais e tente novamente.")
else:
    print("Infelizmente, você foi reprovado. Tente novamente no proximo ano.")
    
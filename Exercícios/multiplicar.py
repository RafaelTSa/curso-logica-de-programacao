def muktiply(a, b):
    return a * b

while True:
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = muktiply(num1, num2)
        print(f"O resultado da multiplicação é: {int(resultado)}")
        break
    except ValueError:
        print("Por favor, digite números válidos.")
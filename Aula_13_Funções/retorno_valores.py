# Retorno de valores

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

# Chamando a função e armazenando o resultado
a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))

resultado = somar (a, b)
print(f"A soma é {resultado}")

resultado = subtrair(a, b)
print(f"A subtração é {resultado}")

resultado = multiplicar(a, b)
print(f"A multiplicação é {resultado}")

resultado = dividir(a, b)
print(f"A divisão é {resultado:.2f}") # :.2f mostra apenas dois números apos a virgula



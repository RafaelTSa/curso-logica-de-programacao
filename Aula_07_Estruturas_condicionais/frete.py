# calcular o preço do frete.

# frete leve <= 2 kg
# frete medio >2 kg e <=5 kg
# frete pesado >5 kg

frete_leve = 15.00
frete_medio = 25.00
frete_pesado = 40.00

peso = float (input("Digite o peso da mercadoria kg:"))

if peso <=2:
    print("O valor do frete é R$:", frete_leve)
elif peso <=5:
    print("O valor do frete é R$:", frete_medio)
else:
    print("O valor do frete é R$:", frete_pesado)
    
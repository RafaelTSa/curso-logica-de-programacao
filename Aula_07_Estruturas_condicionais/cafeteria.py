# Verificar se o dinheiro do cliente é suficiente

# tabela preços
Cappuccino = 10.00
Café_com_leite = 7.00
Café_simples = 4.00

dinheiro = float(input("Digite quanto dinheiro tem (R$): "))

if dinheiro >= Cappuccino:
    print("Você pode pedir o cappuccino.")
elif dinheiro >= Café_com_leite:
    print("Você pode pedir café com leite.")
elif dinheiro >= Café_simples:
    print("Você pode pedir um Café simples.")
else:
    print("Desculpe você não tem Dinheiro sufuciênte.")

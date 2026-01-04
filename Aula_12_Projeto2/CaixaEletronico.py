# Simulando um Caixa Eletronico

# O Usuário tem um saldo inicial de R$ 500 e pode
# Sacar dinheiro até zerar o saldo ou encerrar

saldo = 500

while saldo > 0:
    saque = float(input("Informe o valor do saque (ou 0 para encerrar):"))

    if saque == 0:
        break

    if saque > saldo:
        print("Saldo insuficiente! Saque não efetuado.")
    else:
        saldo -= saque
        print(f"Saque efetuado! Novo saldo R$ {saldo:.2f}")

print("Operação encerrada.")
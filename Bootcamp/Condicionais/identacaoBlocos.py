def sacar(valor, saldo):
    if valor <= saldo:
        saldo -= valor
        print(f"Saque de R${valor} realizado com sucesso.")

sacar(100, 150)
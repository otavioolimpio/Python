# Aprendendo sobre encapsulamento em Python!

class Conta:
    def __init__(self, titular, saldo_inicial=0):
        self._saldo = saldo_inicial  # Atributo privado
        self.nome_titular = titular  # Atributo público

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
        else:
            print("Valor de depósito deve ser positivo.")

    def sacar(self, valor):
        if 0 < valor <= self._saldo:
            self._saldo -= valor
        else:
            print("Saldo insuficiente ou valor inválido.")

    def consultar_saldo(self):
        return self._saldo
    
# Exemplo de uso
conta = Conta("João", 1000)
conta.depositar(500)
conta.sacar(200)
print(f"Saldo atual de {conta.nome_titular}: R$ {conta.consultar_saldo()}")
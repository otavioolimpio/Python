# Aprendendo sobre proprieties() em Python!
class Foo:
    def __init__(self, valor):
        self._valor = valor  # Atributo privado

    @property
    def valor(self):
        """Getter para o atributo valor."""
        return self._valor

    @valor.setter
    def valor(self, novo_valor):
        """Setter para o atributo valor."""
        if novo_valor >= 0:
            self._valor = novo_valor
        else:
            print("O valor deve ser não-negativo.")
    @valor.deleter
    def valor(self):
        """Deleter para o atributo valor."""
        self._valor = 0

# Exemplo de uso
foo = Foo(10)
print(f"Valor inicial: {foo.valor}")
foo.valor = 20
print(f"Novo valor: {foo.valor}")
foo.valor = -5  # Tentativa de definir um valor inválido
print(f"Valor após tentativa inválida: {foo.valor}")
del foo.valor
print(f"Valor após deleção: {foo.valor}")
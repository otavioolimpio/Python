# Classes são moldes para criar objetos em Python.
# Elas encapsulam dados e comportamentos relacionados.

# Como exemplo, vamos criar uma classe chamada 'Visitante'.
class Visitante:
    # O método __init__ é o construtor da classe.
    # Ele é chamado quando um novo objeto da classe é criado.
    def __init__(self, nome, idade):
        self.nome = nome  # Atributo 'nome'
        self.idade = idade  # Atributo 'idade'

    # Método para exibir informações do visitante
    def exibir_informacoes(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}")

# Criando um objeto da classe Visitante
visitante1 = Visitante("Alice", 30)
# Usando o método para exibir as informações do visitante
visitante1.exibir_informacoes() # Saída: Nome: Alice, Idade: 30
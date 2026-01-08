# Declarando construtores e destrutores em Python
class Pessoa:
    def __init__(self, nome, idade):
        """Construtor da classe Pessoa."""
        self.nome = nome
        self.idade = idade
        print(f'Pessoa {self.nome} criada com sucesso!')

    def __del__(self):
        """Destrutor da classe Pessoa."""
        print(f'Pessoa {self.nome} destruída!')
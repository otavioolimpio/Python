# Aprendendo sobre Herança em Python
class Animal:
    def __init__(self, nome):
        self.nome = nome
    def fazer_som(self):
        print("Eu faço som: ...")

class Cachorro(Animal):
    def __init__(self, nome, raça):
        super().__init__(nome)
        self.raça = raça

    def fazer_som(self):
        print("Au Au!")

class Gato(Animal):
    def fazer_som(self):
        print("Miau Miau!")

# Criando instâncias das classes
meu_cachorro = Cachorro("Rex", "Labrador")  
meu_gato = Gato("Mimi")

# Chamando o método fazer_som
meu_cachorro.fazer_som()  # Saída: Au Au!
meu_gato.fazer_som()      # Saída: Miau Miau!
# Aprendendo sobre variaveis de classe e de instância em Python
class Carro:
    # Variável de classe
    rodas = 4

    def __init__(self, marca, modelo):
        # Variáveis de instância
        self.marca = marca
        self.modelo = modelo

# Criando instâncias da classe Carro
carro1 = Carro("Toyota", "Corolla")
carro2 = Carro("Honda", "Civic")

# Acessando variáveis de instância
print(f"Carro 1: {carro1.marca} {carro1.modelo}, Rodas: {carro1.rodas}")
print(f"Carro 2: {carro2.marca} {carro2.modelo}, Rodas: {carro2.rodas}")

# Modificando a variável de classe
Carro.rodas = 6
print(f"Após modificar a variável de classe:")
print(f"Carro 1: {carro1.marca} {carro1.modelo}, Rodas: {carro1.rodas}")
print(f"Carro 2: {carro2.marca} {carro2.modelo}, Rodas: {carro2.rodas}")

# Modificando a variável de instância
carro1.rodas = 8
print(f"Após modificar a variável de instância do carro 1:")
print(f"Carro 1: {carro1.marca} {carro1.modelo}, Rodas: {carro1.rodas}")
print(f"Carro 2: {carro2.marca} {carro2.modelo}, Rodas: {carro2.rodas}")
# Definindo a classe Bicicleta
class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join(f'{k}={v}' for k, v in self.__dict__.items())}"

    def buzinar(self):
        print("Buzinando: BEEP BEEP!")
    
    def parar(self):
        print("A bicicleta parou.")

    def correr(self):
        print("A bicicleta está em movimento.")

# Criando uma instância da classe Bicicleta
caloi = Bicicleta("Vermelha", "Caloi 10", 2020, 1500)

caloi.buzinar()
caloi.correr()  
caloi.parar()
print(caloi)
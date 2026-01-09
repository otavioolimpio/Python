# Aprendendo sobre classes abstratas em Python
from abc import ABC, abstractmethod
class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

class ControleTV(ControleRemoto):
    def ligar(self):
        print("TV ligada")

    def desligar(self):
        print("TV desligada")
class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("Ar-condicionado ligado")

    def desligar(self):
        print("Ar-condicionado desligado")

# Testando as classes
controle_tv = ControleTV()
controle_tv.ligar()
controle_tv.desligar()
controle_ar = ControleArCondicionado()
controle_ar.ligar()
controle_ar.desligar()  

# Tentando instanciar a classe abstrata (isso causará um erro)
# controle = ControleRemoto()  # Descomente esta linha para ver o erro
# Saída esperada:
# TV ligada 
# TV desligada
# Ar-condicionado ligado
# Ar-condicionado desligado
# TypeError: Can't instantiate abstract class ControleRemoto with abstract methods desligar, ligar
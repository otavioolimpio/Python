# Aprendendo sobre polimorfismo em Python
class Passaro:
    def voar(self):
        return "O pássaro está voando."
    
class Pardal(Passaro):
    def voar(self):
        print("O pardal está voando baixo.")

class Avestruz(Passaro):
    def voar(self):
        print("A avestruz não pode voar.")

def planejar_voo(objeto_passaro):
    objeto_passaro.voar()


planejar_voo(Pardal())  # Saída: O pardal está voando baixo.
planejar_voo(Avestruz())  # Saída: A avestruz não pode voar.
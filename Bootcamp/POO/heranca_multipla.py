# Vamos aprender sobre herança múltipla em Python!

class Animal:
    def __init__(self, numeo_de_patas):
        self.numero_de_patas = numeo_de_patas

    def __str__(self):
        return f"{self.__class__.__name__}(numero_de_patas={self.numero_de_patas})"

class Ave(Animal):
   def __init__(self, numeo_de_patas, pode_voar):
        super().__init__(numeo_de_patas)
        self.pode_voar = pode_voar

class Mamifero(Animal):
    def __init__(self, numeo_de_patas, tem_pelo):
        super().__init__(numeo_de_patas)
        self.tem_pelo = tem_pelo

# chamando a herança múltipla
class Morcego(Ave, Mamifero):
    def __init__(self, numeo_de_patas, pode_voar, tem_pelo):
        Ave.__init__(self, numeo_de_patas, pode_voar)
        Mamifero.__init__(self, numeo_de_patas, tem_pelo)
    def __str__(self):
        return (f"{self.__class__.__name__}(numero_de_patas={self.numero_de_patas}, "
                f"pode_voar={self.pode_voar}, tem_pelo={self.tem_pelo})")
    
# Criando uma instância de Morcego
morcego = Morcego(numeo_de_patas=2, pode_voar=True, tem_pelo=True)
print(morcego)

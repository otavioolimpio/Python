# Aprendendo sobre metodos de classe e estaticos em Python
class Pessoa:
    def __init__(self,nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_bebe(cls, nome):
        return cls(nome, 0)
    
    @staticmethod
    def eh_maior_idade(idade):
        return idade >= 18  
    
# Criando uma instancia de Pessoa usando o metodo de classe
bebe = Pessoa.criar_bebe("João")    
print(f'Nome: {bebe.nome}, Idade: {bebe.idade}')  # Saída: Nome: João, Idade: 0

# Verificando se uma idade é maior de idade usando o metodo estatico
print(Pessoa.eh_maior_idade(20))  # Saída: True 
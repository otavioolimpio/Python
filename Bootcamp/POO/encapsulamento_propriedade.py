# Criando a classe Pessoa com encapsulamento de propriedade
class Pessoa:
    def __init__(self, nome, data_nascimento):
        self._nome = nome  # Atributo privado
        self._data_nascimento = data_nascimento  # Atributo privado
    
    @property
    def nome(self):
        """Getter para o atributo nome."""
        return self._nome
    
    @property
    def idade(self):
        """Calcula a idade com base na data de nascimento."""
        from datetime import datetime
        hoje = datetime.now()
        ano_nascimento = int(self._data_nascimento.split('-')[0])
        return hoje.year - ano_nascimento
    
# Exemplo de uso
pessoa = Pessoa("Ana", "1990-05-15")
print(f"Nome: {pessoa.nome}")
print(f"Idade: {pessoa.idade} anos")
# Entendendo os metodos de dicionários em Python
meu_dicionario = {
    "nome": "Alice",        
    "idade": 30,
    "cidade": "São Paulo"
}   

# Método get(): Retorna o valor para a chave especificada
nome = meu_dicionario.get("nome")
print("Nome:", nome)  # Saída: Nome: Alice  

# Método keys(): Retorna uma visão das chaves no dicionário
chaves = meu_dicionario.keys()
print("Chaves:", chaves)  # Saída: Chaves: dict_keys(['nome', 'idade', 'cidade'])

# Método values(): Retorna uma visão dos valores no dicionário
valores = meu_dicionario.values()
print("Valores:", valores)  # Saída: Valores: dict_values(['Alice', 30, 'São Paulo'])

# Método items(): Retorna uma visão dos pares chave-valor no dicionário
itens = meu_dicionario.items()
print("Itens:", itens)  # Saída: Itens: dict_items([('nome', 'Alice'), ('idade', 30), ('cidade', 'São Paulo')])

# Método pop(): Remove a chave especificada e retorna seu valor
idade = meu_dicionario.pop("idade")
print("Idade removida:", idade)  # Saída: Idade removida: 30
print("Dicionário após pop:", meu_dicionario)  # Saída: Dicionário após pop: {'nome': 'Alice', 'cidade': 'São Paulo'}

# Método update(): Atualiza o dicionário com os pares chave-valor de outro dicionário
meu_dicionario.update({"profissão": "Engenheira", "idade": 31})
print("Dicionário após update:", meu_dicionario)  # Saída: Dicionário após update: {'nome': 'Alice', 'cidade': 'São Paulo', 'profissão': 'Engenheira', 'idade': 31}

# Método clear(): Remove todos os itens do dicionário
meu_dicionario.clear()
print("Dicionário após clear:", meu_dicionario)  # Saída: Dicionário após clear: {}

# Método copy(): Retorna uma cópia rasa do dicionário
meu_dicionario = {
    "nome": "Alice",        
    "idade": 30,
    "cidade": "São Paulo"
}
copia_dicionario = meu_dicionario.copy()
print("Cópia do dicionário:", copia_dicionario)  # Saída: Cópia do dicionário: {'nome': 'Alice', 'idade': 30, 'cidade': 'São Paulo'}    

# Método setdefault(): Retorna o valor da chave especificada. Se a chave não existir, insere a chave com o valor padrão fornecido
cidade = meu_dicionario.setdefault("cidade", "Rio de Janeiro")
print("Cidade:", cidade)  # Saída: Cidade: São Paulo
pais = meu_dicionario.setdefault("país", "Brasil")





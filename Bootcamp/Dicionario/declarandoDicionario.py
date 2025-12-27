# Declarando um dicionário em Python
# Dicionários são estruturas de dados mutáveis que armazenam pares de chave-valor   
# Eles são definidos usando chaves {}
# Exemplo de declaração de um dicionário    

meu_dicionario = {
    "nome": "Alice",    
    "idade": 30,
    "cidade": "São Paulo"
}   

# Imprimindo o dicionário
print(meu_dicionario)

# Acessando valores no dicionário usando chaves
print("Nome:", meu_dicionario["nome"])  
print("Idade:", meu_dicionario["idade"])
print("Cidade:", meu_dicionario["cidade"])

# Adicionando um novo par chave-valor ao dicionário
meu_dicionario["profissão"] = "Engenheira"  
print("Dicionário atualizado:", meu_dicionario)

# Modificando um valor existente no dicionário
meu_dicionario["idade"] = 31
print("Idade atualizada:", meu_dicionario["idade"])

# Removendo um par chave-valor do dicionário
del meu_dicionario["cidade"]
print("Dicionário após remoção:", meu_dicionario)

# Iterando sobre o dicionário
for chave, valor in meu_dicionario.items():
    print(f"{chave}: {valor}")

# Verificando se uma chave existe no dicionário
if "nome" in meu_dicionario:
    print("A chave 'nome' existe no dicionário.")
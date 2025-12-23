nome = "Otavio Olimpio da Silva Medeiros"

print(nome[0:6])  # Fatiamento do índice 0 ao 6
print(nome[7:14]) # Fatiamento do índice 7 ao 14
print(nome[15:17]) # Fatiamento do índice 15 ao 17
print(nome[18:26:2]) # Fatiamento do índice 18 ao 26 com passo 2
print(nome[:6])   # Fatiamento do início ao índice 6
print(nome[7:])   # Fatiamento do índice 7 até o final
print(nome[:])    # Fatiamento de toda a string
print(nome[::2])  # Fatiamento com passo 2 (caracteres em posições pares)
print(nome[1::2]) # Fatiamento com passo 2 (caracteres em posições ímpares)
print(nome[::-1]) # Fatiamento invertido (string ao contrário)
print(nome[::-2]) # Fatiamento invertido com passo 2 (caracteres em posições pares ao contrário)
print(nome[-1::-1]) # Fatiamento invertido usando índice negativo
print(nome[-1:-10:-1]) # Fatiamento invertido de índices negativos
print(nome[-10:]) # Fatiamento dos últimos 10 caracteres
print(nome[:-10]) # Fatiamento do início até os últimos 10 caracteres
print(nome[-15:-5]) # Fatiamento de índices negativos
print(nome[-15:5]) # Fatiamento de índice negativo até índice positivo
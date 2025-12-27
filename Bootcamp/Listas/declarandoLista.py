frutas = ["maça", "banana", "laranja", "uva"]
print(frutas[0])  # Acessa o primeiro elemento da lista
print(frutas[-1])  # Acessa o último elemento da lista

matrizes = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrizes[1][2])  # Acessa o elemento na segunda linha e terceira coluna da matriz
print(matrizes[0][0])  # Acessa o elemento na primeira linha e primeira coluna da matriz
print(matrizes[-1][-1])  # Acessa o último elemento da última linha da matriz

# Fatiamento de listas
print(frutas[1:3])  # Acessa elementos do índice 1 ao 2 (exclusivo)
print(frutas[:2])   # Acessa os dois primeiros elementos
print(frutas[2:])   # Acessa do índice 2 até o final da lista
print(frutas[-3:])  # Acessa os últimos três elementos da lista

print(matrizes[0][1:3])  # Acessa elementos da primeira linha, do índice 1 ao 2 (exclusivo)
print(matrizes[1][:2])    # Acessa os dois primeiros elementos da segunda linha
print(matrizes[2][1:])    # Acessa do índice 1 até o final da terceira linha
print(matrizes[0:2:2])  # Acessa as primeiras duas linhas da matriz
print(matrizes[::-1])  # Inverte a ordem das linhas da matriz
print(matrizes[::2])  # Acessa todas as linhas da matriz com passo 2

# List compreensão
quadrados = [x**2 for x in range(10)]
print(quadrados)  # Imprime os quadrados dos números de 0 a 9

pares = [x for x in range(20) if x % 2 == 0]
print(pares)  # Imprime os números pares de 0 a 19
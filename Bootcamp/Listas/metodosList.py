# metodo append: Agrega um elemento ao final da lista
lista = [1, 2, 3]
lista.append(4) 
print("Após append:", lista)  # Saída: [1, 2, 3, 4]

# metodo insert: Insere um elemento em uma posição específica
lista.insert(1, 1.5)    
print("Após insert:", lista)  # Saída: [1, 1.5, 2, 3, 4]

# metodo remove: Remove a primeira ocorrência de um elemento
lista.remove(1.5)  
print("Após remove:", lista)  # Saída: [1, 2, 3, 4]

# metodo pop: Remove e retorna o último elemento da lista
ultimo_elemento = lista.pop()
print("Após pop:", lista)  # Saída: [1, 2, 3]
print("Elemento removido com pop:", ultimo_elemento)  # Saída: 4

# metodo clear: Remove todos os elementos da lista
lista.clear()   
print("Após clear:", lista)  # Saída: []

# metodo extend: Adiciona todos os elementos de outra lista ao final da lista atual
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista1.extend(lista2)  
print("Após extend:", lista1)  # Saída: [1, 2, 3, 4, 5, 6]

# metodo index: Retorna o índice da primeira ocorrência de um elemento
indice = lista1.index(4)
print("Índice do elemento 4:", indice)  # Saída: 3  

# metodo count: Retorna o número de ocorrências de um elemento na lista
ocorrencias = lista1.count(2)
print("Ocorrências do elemento 2:", ocorrencias)  # Saída: 1

# metodo sort: Ordena os elementos da lista em ordem crescente
lista1.sort()
print("Após sort:", lista1)  # Saída: [1, 2, 3, 4, 5, 6]

# metodo reverse: Inverte a ordem dos elementos na lista
lista1.reverse()
print("Após reverse:", lista1)  # Saída: [6, 5, 4, 3, 2, 1]

# metodo copy: Retorna uma cópia rasa da lista
lista_copia = lista1.copy()
print("Cópia da lista:", lista_copia)  # Saída: [6, 5, 4, 3, 2, 1]

# metodo len: Retorna o número de elementos na lista
tamanho = len(lista1)
print("Tamanho da lista:", tamanho)  # Saída: 6

# metodo sum: Retorna a soma dos elementos da lista
soma = sum(lista1)
print("Soma dos elementos da lista:", soma)  # Saída: 21

# metodo min: Retorna o menor elemento da lista
menor = min(lista1)
print("Menor elemento da lista:", menor)  # Saída: 1

# metodo max: Retorna o maior elemento da lista
maior = max(lista1)
print("Maior elemento da lista:", maior)  # Saída: 6

# metodo slice: Retorna uma sublista a partir de índices especificados
sublista = lista1[1:4]  
print("Sublista (índices 1 a 3):", sublista)  # Saída: [5, 4, 3]

# metodo join: Concatena os elementos da lista em uma única string, separados por um delimitador
lista_strings = ['Olá', 'mundo', 'de', 'Python']    
frase = ' '.join(lista_strings)  
print("Após join:", frase)  # Saída: "Olá mundo de Python"

# metodo split: Divide uma string em uma lista de substrings com base em um delimitador
frase = "Olá mundo de Python"
lista_dividida = frase.split(' ')
print("Após split:", lista_dividida)  # Saída: ['Olá', 'mundo', 'de', 'Python']

# metodo enumerate: Retorna um objeto enumerado que contém pares índice-valor da lista
lista_enumerada = list(enumerate(['a', 'b', 'c']))  
print("Após enumerate:", lista_enumerada)  # Saída: [(0, 'a'), (1, 'b'), (2, 'c')]

# metodo zip: Combina elementos de duas ou mais listas em tuplas
lista_a = [1, 2, 3]
lista_b = ['a', 'b', 'c']
combinada = list(zip(lista_a, lista_b))
print("Após zip:", combinada)  # Saída: [(1, 'a'), (2, 'b'), (3, 'c')]
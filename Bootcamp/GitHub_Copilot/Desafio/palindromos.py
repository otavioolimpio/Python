# Recebe uma palavra como entrada
palavra = input("Digite uma palavra: ").lower()

# Inverte a palavra usando manipulação de strings
palavra_invertida = palavra[::-1]

# Verifica se é um palíndromo
if palavra == palavra_invertida:
    print(f"A palavra '{palavra}' é um palíndromo.")
else:
    print(f"A palavra '{palavra}' não é um palíndromo.")
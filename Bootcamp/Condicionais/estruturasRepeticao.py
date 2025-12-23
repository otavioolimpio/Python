texto = input("Digite um texto: ")
VOGAIS = "AEIOU"

# Usando o for para iterar sobre cada letra do texto
for letra in texto:
    if letra.upper() in VOGAIS:
        print(f"{letra} é uma vogal.")
    else:
        print(f"{letra} é uma consoante.")

# Usando o range para iterar sobre os índices do texto
for i in range(len(texto)):
    letra = texto[i]
    if letra.upper() in VOGAIS:
        print(f"Índice {i}: {letra} é uma vogal.")
    else:
        print(f"Índice {i}: {letra} é uma consoante.")

# Usando o while para iterar sobre o texto
index = 0
while index < len(texto):
    letra = texto[index]
    if letra.upper() in VOGAIS:
        print(f"Índice {index}: {letra} é uma vogal.")
    else:
        print(f"Índice {index}: {letra} é uma consoante.")
    index += 1
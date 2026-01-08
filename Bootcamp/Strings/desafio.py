def entrada(texto):
    novo = texto.strip().lower()
    novo = ' '.join(novo.split())
    return novo

texto = " Bem  Vindo Ao  LAB "
print(entrada(texto))  # Saída: "bem vindo ao lab"
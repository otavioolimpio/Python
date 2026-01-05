try:
    with open('exemplo.txt', 'r') as arquivo:
        conteudo = arquivo.read()
        print(conteudo)
except IOError as e:
    print(f'Erro ao abrir o arquivo: {e}')

try:
    with open("meu-texto.txt", encoding="utf-8") as arquivo: # Especifica a codificação ao abrir o arquivo
        conteudo = arquivo.read()
        print(conteudo)
except IOError as e:
    print(f'Erro ao abrir o arquivo: {e}')
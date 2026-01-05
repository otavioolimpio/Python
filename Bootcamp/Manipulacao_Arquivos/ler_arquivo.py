# Lendo o conteúdo de um arquivo texto em Python
file = open('C:\\Users\\otavio\\Documents\\GitHub\\Python\\Bootcamp\\Manipulacao_Arquivos\\loren.txt', 'r')  # Abre o arquivo em modo de leitura
#conteudo = file.read()           # Lê todo o conteúdo do arquivo
#conteudo = file.readlines()      # Lê todas as linhas do arquivo como uma lista
conteudo = file.readline()        # Lê uma única linha do arquivo
print(conteudo)                   # Imprime o conteúdo lido

for linha in conteudo:
    print(linha)                 # Imprime cada linha individualmente

# Outra forma de ler arquivos usando 'with', que fecha o arquivo automaticamente
with open('C:\\Users\\otavio\\Documents\\GitHub\\Python\\Bootcamp\\Manipulacao_Arquivos\\loren.txt', 'r') as file:
    conteudo = file.read()
    print(conteudo)

while len(linha := file.readline()) > 0:  # Lê linha por linha até o final do arquivo
    print(linha)                          # Imprime cada linha lida
file.close()                              # Fecha o arquivo


# Observação: readlines armazena todas as linhas em forma de lista, o que pode consumir muita memória para arquivos grandes.
file = open('C:\\Users\\otavio\\Documents\\GitHub\\Python\\Bootcamp\\Manipulacao_Arquivos\\loren.txt', 'r')  # Abre o arquivo em modo de leitura
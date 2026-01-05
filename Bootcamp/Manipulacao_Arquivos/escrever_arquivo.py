arquivo = open('C:\\Users\\otavio\\Documents\\GitHub\\Python\\Bootcamp\\Manipulacao_Arquivos\\escrever.txt', 'w')
arquivo.write('Me chamo Otavio\n') # Escreve no arquivo
arquivo.write('Estou aprendendo Python\n') # Escreve no arquivo
arquivo.writelines(['Linha 1\n', 'Linha 2\n', 'Linha 3\n']) # Escreve várias linhas no arquivo
arquivo.close()

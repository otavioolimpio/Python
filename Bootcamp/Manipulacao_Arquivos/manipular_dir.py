# manipulação de diretórios em Python
import os
import shutil

from pathlib import Path
ROOT_PATH = Path(__file__).parent

# criando um diretório
# os.mkdir(ROOT_PATH / 'novo_diretorio')

# arquivo = open(ROOT_PATH / 'novo_diretorio' / 'arquivo.txt', 'w')  # criando um arquivo dentro do diretório
# arquivo.write('Linha 1\n')
# arquivo.write('Linha 2\n')  
# arquivo.close()

# os.rename(ROOT_PATH / 'diretorio_renomeado', ROOT_PATH / 'novo_diretorio')  # renomeia diretório
# os.rmdir(ROOT_PATH / 'diretorio_renomeado')  # só remove diretórios vazios
# os.remove(ROOT_PATH / 'novo_diretorio' / 'arquivo.txt')  # remove arquivos diretórios com arquivos dentro
arquivo = open(ROOT_PATH / 'novo_diretorio' / 'novo.txt', 'w')  # criando um arquivo dentro do diretório
shutil.move(ROOT_PATH / 'novo_diretorio' / 'novo.txt', ROOT_PATH / )  # move diretórios com arquivos dentro

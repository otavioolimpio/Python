# Tratando os possiveis erros ao manipular arquivos
try:
    with open('arquivo_inexistente.txt', 'r') as arquivo:
        conteudo = arquivo.read()
        print(conteudo)
except FileNotFoundError:
    print("Erro: O arquivo não foi encontrado.")

except IOError:
    print("Erro: Problema ao ler o arquivo.")   
except Exception as e:
    print(f"Erro inesperado: {e}")
finally:
    print("Execução do bloco try-except finalizada.")

# Tentando abrir um diretorio como se fosse um arquivo
try:    
    with open('diretorio_exemplo', 'r') as arquivo:
        conteudo = arquivo.read()
        print(conteudo) 
except IsADirectoryError:
    print("Erro: Esperava um arquivo, mas um diretório foi fornecido.")
except Exception as e:
    print(f"Erro inesperado: {e}")  
finally:
    print("Execução do bloco try-except finalizada.")
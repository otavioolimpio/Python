import os
from enigma import Enigma

# 1. Configurações da Máquina (Entradas do usuário)
rotores_escolhidos = [5, 4, 1]   # Ex: Rotor I à esquerda, II no centro, III à direita
posicoes_iniciais  = [7, 10, 11]   # Ex: Posição A, A, A (Equivalente a 1, 1, 1)

# Nome do arquivo de texto
nome_arquivo = "mensagem.txt"

# Criando um arquivo de teste rápido caso ele não exista
if not os.path.exists(nome_arquivo):
    with open(nome_arquivo, "w") as f:
        f.write("AALERTAREIAGUARDAPOSICAONORTE")  # Texto limpo do usuário aprovado
    print(f"Criado arquivo '{nome_arquivo}' para testes.\n")

# 2. Lendo o arquivo txt contendo a mensagem
with open(nome_arquivo, "r") as f:
    mensagem_original = f.read().strip()

print(f"Configuração Inicial -> Rotores: {rotores_escolhidos} | Posições: {posicoes_iniciais}")
print(f"Texto Original:       {mensagem_original}")

# 3. Inicializa a máquina para CRIPTOGRAFAR
enigma_cifrar = Enigma(rotores_escolhidos, posicoes_iniciais)
texto_criptografado = enigma_cifrar.cifrar_texto(mensagem_original)
print(f"Texto Criptografado:  {texto_criptografado}")

# 4. Inicializa NOVA instância idêntica para DESCRIPTOGRAFAR
enigma_decifrar = Enigma(rotores_escolhidos, posicoes_iniciais)
texto_decifrado = enigma_decifrar.cifrar_texto(texto_criptografado)
print(f"Texto Decifrado:       {texto_decifrado}")
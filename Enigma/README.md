# Simulador da Máquina Enigma

Este projeto é uma implementação fiel em Python da famosa **Máquina Enigma**, a ferramenta de criptografia eletromecânica utilizada pela Alemanha durante a Segunda Guerra Mundial. O projeto lê uma mensagem real de um estudante de Licenciatura em Computação a partir de um arquivo de texto, cifra os dados usando rotores e em seguida, decifra a mensagem para provar a simetria do sistema.

---

## 📁 Estrutura do Projeto

O projeto é composto por 3 arquivos principais:

1. **`enigma.py`**: Arquivo contendo a classe principal `Enigma`. Ele gerencia os dicionários de fiação dos rotores (I ao V), o refletor B e a lógica matemática de rotação.
2. **`main.py`**: Script responsável por configurar os parâmetros da máquina, verificar a existência do arquivo de texto, inicializar os objetos e exibir os resultados na tela.
3. **`mensagem.txt`**: O arquivo de entrada que armazena a mensagem secreta a ser processada.

---

## 🚀 Como Funciona a Criptografia Enigma?

A Enigma baseia-se em um circuito elétrico fechado. O grande segredo do código implementado é a **simetria perfeita**: se você configurar a máquina de uma forma e digitar uma letra, ela gerará um caractere embaralhado. Se você pegar uma máquina idêntica, com a **mesma configuração inicial**, e digitar o caractere embaralhado, ela revelará a letra original.

O fluxo do sinal elétrico simulado no código segue este caminho:
1. **Avanço Mecânico:** Os rotores giram *antes* do sinal passar.
2. **Caminho de Ida:** Teclado ➡️ Rotor Direita ➡️ Rotor Centro ➡️ Rotor Esquerda.
3. **Refletor (Refletor B):** O sinal bate no espelho e inverte o sentido.
4. **Caminho de Volta:** Rotor Esquerda ➡️ Rotor Centro ➡️ Rotor Direita ➡️ Lâmpada de Saída.

---

## ⚙️ Conceitos de Computação Aplicados

Como um projeto voltado para a área de **Licenciatura em Computação**, este código serve como um excelente recurso pedagógico para ilustrar:
* **Aritmética Modular:** Uso do operador `% 26` para simular o comportamento circular das engrenagens e do alfabeto.
* **Programação Orientada a Objetos (POO):** Encapsulamento de estados (`self.pos_esq`, `self.pos_cen`, etc.) e reaproveitamento de classes (múltiplas instâncias).
* **Manipulação de Arquivos (I/O):** Leitura e escrita persistente de arquivos de texto nativos com Python.
* **História da Computação:** Uma conexão direta com os estudos de criptoanálise de Alan Turing em Bletchley Park, fundamentais para o surgimento dos primeiros computadores.

---

## 💻 Como Executar e Usar

### Pré-requisitos
* Ter o **Python 3.x** instalado.

### Configuração do Arquivo de Texto
Certifique-se de que o arquivo `mensagem.txt` esteja na mesma pasta do seu código com o seguinte conteúdo limpo (sem espaços ou acentos):
```text
MEUNOMEEOTAVIOSOUESTUDANTEDELICENCIATURAEMCOMPUTACAO
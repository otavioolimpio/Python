# Resolução do Desafio: Sistema Bancário em Python ✅ 
## 📌 Visão Geral

Este repositório contém a **resolução completa do desafio de otimização de um Sistema Bancário**, utilizando **funções em Python** para organizar, estruturar e tornar o código mais eficiente e legível.

A solução implementa as principais operações bancárias — **cadastro de clientes, criação de conta corrente, depósito, saque e extrato** — aplicando conceitos fundamentais de programação estruturada e boas práticas da linguagem Python.

---

## 🎯 Objetivo da Resolução

O objetivo desta resolução foi:

* Refatorar o sistema bancário original
* Dividir as responsabilidades do sistema em **funções bem definidas**
* Facilitar a manutenção e o entendimento do código
* Demonstrar domínio de funções, parâmetros posicionais e nomeados

---

## 🧠 Estratégia de Implementação

A solução foi desenvolvida seguindo os princípios abaixo:

* Cada operação do sistema foi encapsulada em uma função específica
* Uso de **listas de dicionários** para armazenar clientes e contas
* Controle de regras de negócio (limites, número de saques, validações)
* Menu interativo para navegação do usuário

---

## ⚙️ Funcionalidades Implementadas

### 👤 Cadastro de Usuário

Função responsável por cadastrar clientes no sistema, evitando duplicidade de CPF.

**Função:** `usuario(cliente, lista_cliente)`

* Valida se o CPF já existe
* Insere o cliente na lista
* Retorna `True` ou `False` conforme o resultado

---

### 🏦 Conta Corrente

Criação de conta corrente associada a um usuário existente.

**Função:** `conta_corrente(agencia, numero_conta, usuario)`

* Incrementa o número da conta
* Associa a conta ao usuário

---

### ➕ Depósito

Permite adicionar valores positivos ao saldo da conta.

**Função:** `deposito(saldo_conta, valor_deposito)`

* Atualiza o saldo
* Registra a operação no extrato

---

### ➖ Saque

Realiza saques respeitando regras de negócio.

**Função:** `saque(saldo_conta, valor_saque, limite_conta, numero_saque, limite_saque)`

* Verifica saldo disponível
* Respeita limite por saque
* Controla quantidade máxima de saques
* Atualiza saldo e extrato

---

### 📄 Extrato

Exibe o histórico de movimentações realizadas na conta.

**Função:** `historico(saldo, valor, operacao)`

* Registra depósitos e saques
* Atualiza o extrato global

---

## 🔄 Menu de Operações

O sistema utiliza um **menu interativo** que permite ao usuário:

* Criar conta
* Listar clientes
* Criar conta corrente
* Consultar saldo
* Realizar depósitos e saques
* Visualizar extrato
* Encerrar o sistema

---

## 🧩 Estrutura de Dados Utilizada

* `lista_clientes`: lista de dicionários contendo dados dos clientes
* `lista_contas`: lista contendo contas associadas aos usuários
* Variáveis de controle para saldo, limite e número de saques
---

## ✅ Resultado Final

Ao final da implementação, obteve-se um sistema bancário:

* Funcional
* Modularizado
* Organizado
* Fácil de entender e manter
---

## ✍️ Autor

Resolução desenvolvida por **Otávio Olímpio**

---

📚 Desafio concluído com sucesso

# ************************** Declarando Funcoes **************************
# Declarando a funcao usuario
def usuario(cliente, lista_cliente):
    for id in lista_cliente:
        if cliente["cpf"] == id["cpf"]:
            print(f"Cliente {cliente['nome']} já possui cadastro")
            return False

    lista_cliente.append(cliente)
    print(f"Cliente {cliente['nome']} cadastrado com sucesso!")
    return True

# Declarando a funcao conta corrente
def conta_corrente(agencia, numero_conta, usuario):
    numero_conta += 1
    print("Conta Corrente criada com sucesso!")
    return agencia, numero_conta, usuario

# Declarando a funcao de extrato
def historico(saldo,/,*, valor, operacao):
    # Mesmo com a recomendação de evitar usar variáveis globais, usei para demonstrar que aprendi
    global extrato
    movimentacoes = (f"Operação realizada:{operacao}, Valor: {valor}, Saldo em Conta: {saldo}\n")
    extrato += movimentacoes

# Declarando a funcao de saque
def saque(*, saldo_conta, valor_saque, limite_conta, numero_saque, limite_saque):

    # Verificando erros ou realizando o saque
    if valor_saque > saldo_conta:
        print("Operação falhou! Você não tem saldo suficiente.")
        return saldo_conta, numero_saque

    elif valor_saque > limite_conta:
        print("Operação falhou! O valor do saque excede o limite.")
        return saldo_conta, numero_saque

    elif numero_saque >= limite_saque:
        print("Operação falhou! Número máximo de saques excedido.")
        return saldo_conta, numero_saque

    elif valor_saque > 0:
        saldo_conta -= valor_saque
        historico(saldo_conta, valor = valor_saque, operacao="saque")
        numero_saque += 1

        return saldo_conta, numero_saque

    else:
        print("Operação falhou! O valor informado é inválido.")

# Declarando a funcao deposito
def deposito(saldo_conta, valor_deposito, /):

    # Atualizando saldo
    update_saldo = saldo_conta + valor_deposito

    # Atualizando extrato
    historico(update_saldo, valor=valor_deposito, operacao="deposito")

    return update_saldo


# ************************** Menu de opcoes **************************
menu = """

[c] Criar Conta
[lc] Listar clientes
[cc] Conta Corrente
[sa} Saldo em conta
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """
# ************************** Declarando Variaveis **************************
saldo = 0
limite = 1000
extrato = "Saldo em conta R$ 0,0\n"
numero_saques = 0
LIMITE_SAQUES = 3
AGENCIA = "0001"
numero_conta = 0
lista_contas = []
lista_clientes = []

while True:

    opcao = input(menu)

    # Opcao para criar uma nova conta para um usuario
    if opcao == "c":

        # Criando dicionario para inserir dados do cadastro
        cadastro_usuario = {

            "nome" : input("Informe seu nome:"),
            "data_nasc" : input("Informe sua data de nascimento dd/mm/aaaa:"),
            "cpf": int(input("Informe seu CPF:")),
            "endereco" : input("Informe seu endereço logradouro - bairro - cidade/ES")
        }

        usuario(cadastro_usuario, lista_clientes)

    # Opcao para criar uma conta corrente e atribuir a um usuario existente
    elif opcao == "cc":

        cpf = int(input("Informe seu CPF:"))
        for id in lista_clientes:
            if cpf == id["cpf"]:
                lista_contas.append(conta_corrente(AGENCIA, numero_conta, id))
            else:
                print("Usuario desejado não possui conta cadastro!")

    # Opcao de listar clientes
    elif opcao == "lc":
        for conta in lista_clientes:
            print(conta["nome"])

    # Opcao de verificar saldo
    elif opcao == "sa":
        print(f"Saldo em conta R${saldo}")

    # Opcao de realizar saque
    elif opcao == "s":

        # Solicitando valor de saque
        valor = float(input("Informe o valor do saque: "))
        sacar = saque(saldo_conta=saldo, valor_saque=valor, limite_conta=limite,
                      numero_saque=numero_saques, limite_saque=LIMITE_SAQUES)
        # Update após realizar o saque
        saldo, numero_saques = sacar

    # Opcao de  realizar deposito
    elif opcao == "d":

        valor = float(input("Informe o valor do deposito:"))

        # Verificando validade do dado inserido
        if valor > 0:
            dep = deposito(saldo, valor)
            saldo = dep
        else:
            print("Informe um valor válido!")

    # Opcao de exibir extrato
    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print(extrato)
        print("\n=========================================")

    # Opcao de encerrar o menu
    elif opcao == "q":
        break

    # Caso a opcao nao seja valida retorna essa mensagem
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
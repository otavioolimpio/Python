# Geradores em Python são funções que utilizam a palavra-chave 'yield' para retornar um valor e pausar sua execução,
# permitindo que a função seja retomada posteriormente. Eles são úteis para economizar memória, pois não armazenam todos os valores na memória de uma vez,
# mas geram os valores sob demanda.

def meu_gerador(numeros: list[int]):

    for numero in numeros:
        yield numero * 2

for i in meu_gerador(numeros = [1, 2, 3]):
    print(i) 
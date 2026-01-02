# decoradores com argumentos
def verifica_primeiro_argumento(valor):
    def interna(funcao):
        def outra(*args, **kwargs):
            if args and args[0] != valor:
                return f"Primeiro argumento precisa ser {valor}"
            return funcao(*args, **kwargs)
        return outra
    return interna

@verifica_primeiro_argumento(10)
def soma_dez(a, b):
    return a + b
print(soma_dez(10, 5))  # Saída: 15
print(soma_dez(5, 5))   # Saída: Primeiro argumento precisa ser 10
# Importante: Lembre-se de que ao usar decoradores com argumentos, você precisa de um nível extra de funções para aceitar os argumentos do decorador.
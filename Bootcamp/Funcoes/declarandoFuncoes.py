# Declarando Funções em Python

# Escopo Global e Local
x = 10  # Variável global
def minha_funcao():
    y = 5  # Variável local
    return x + y  # Acessando variável global dentro da função

# Função para saudar uma pessoa
def saudacao(nome):
    return f"Olá, {nome}! Seja bem-vindo(a)!"

# Função para somar dois números
def soma(a, b):
    return a + b

# Função para calcular o fatorial de um número
def fatorial(n):    
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)
    
# Testando as funções
print(saudacao("Maria")) # Saída: Olá, Maria! Seja bem vindo(a)!
print(soma(5, 3))       # Saída: 8
print(fatorial(5))      # Saída: 120    

# Testando Args e Kwargs
def exemplo_args_kwargs(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

# Chamando a função com args e kwargs
exemplo_args_kwargs(1, 2, 3, nome="João", idade=30)

# Funcção com posicionais e nomeados
def funcao_mista(a, b, /, c, d, *, e, f):
    return a + b + c + d + e + f    

# Testando a função mista
resultado = funcao_mista(1, 2, 3, 4, e=5, f=6)
print("Resultado da função mista:", resultado) # Saída: 21

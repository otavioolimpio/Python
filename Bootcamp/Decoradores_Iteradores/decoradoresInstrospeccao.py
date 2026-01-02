# Decoradores e Introspecção
import functools

def meu_decorador(funcao):
    
    @functools.wraps(funcao)
    def envelope(*args, **kwargs):
        funcao(*args, **kwargs)
        
    return envelope

@meu_decorador
def diz_ola(nome):  
    print(f"Olá, {nome}!")

diz_ola(diz_ola.__name__)  # Saída: diz_ola
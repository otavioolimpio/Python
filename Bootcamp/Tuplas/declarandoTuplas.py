# Declarando tuplas em Python
# Tuplas são estruturas de dados imutáveis que podem armazenar múltiplos valores
# Elas são definidas usando parênteses ()
# Exemplo de declaração de uma tupla
minha_tupla = (1, 2, 3, "quatro", "cinco")
# Imprimindo a tupla
print(minha_tupla)

# Acessando elementos da tupla
print(minha_tupla[0])  # Primeiro elemento
print(minha_tupla[3])  # Quarto elemento

# Tentando modificar um elemento da tupla (isso causará um erro)
# minha_tupla[1] = 10  # Descomente esta linha para ver o erro
# Tuplas são imutáveis, então a linha acima gerará um TypeError
# Podemos criar uma tupla com um único elemento adicionando uma vírgula
tupla_um_elemento = (42,)
print(tupla_um_elemento)

# Tuplas podem conter diferentes tipos de dados
tupla_mista = (1, "dois", 3.0, True)
print(tupla_mista)

# Podemos desempacotar tuplas em variáveis
a, b, c, d, e = minha_tupla
print(a, b, c, d, e)

# Tuplas podem ser usadas para retornar múltiplos valores de uma função
def retorna_tupla():
    return (10, 20, 30)
x, y, z = retorna_tupla()
print(x, y, z)

# Tuplas são úteis para armazenar dados que não devem ser alterados
coordenadas = (40.7128, -74.0060)  # Coordenadas de Nova York
print(coordenadas)  

# Fim do código
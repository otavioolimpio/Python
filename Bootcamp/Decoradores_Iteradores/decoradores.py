# Funções dentro de funções (funções aninhadas)
def diga_ola(nome):
    print(f"Olá, {nome}!")

    def funcao_interna():
        print("Esta é uma função interna.")
    
    def interna_2():
        print("Esta é outra função interna.")
    
    funcao_interna()
    interna_2()

diga_ola("Maria")

def calculadora(funcao):
    def soma(a, b):
        return a + b
    def subtracao(a, b):
        return a - b
    def multiplica(a, b):
        return a * b
    def divide(a, b):
        return a / b
    
    match funcao:
        case "+":
            return soma
        case "-":
            return subtracao
        case "*":
            return multiplica
        case "/":
            return divide   

operacao = calculadora("+")
print(operacao(10, 5))  # Saída: 15

# Decoradores 
def mestre(funcao):
    def aprendiz():
        print("Antes da função ser executada.")
        funcao()
        print("Depois da função ser executada.")
    return aprendiz

print("+++++++++++++++++++++++sem o @mestre+++++++++++++++++++++++")

# sem o @mestre
def diz_ola():
    print("Olá!")
oi = mestre(diz_ola)
oi()

print("+++++++++++++++++++# com o @mestre +++++++++++++++++++++")

# com o @mestre
@mestre 
def diz_oi():
    print("Oi!")
diz_oi()
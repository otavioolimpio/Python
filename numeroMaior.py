#Esse programa destina-se a verificação de qual número é maior em uma entrada com dois valores.

#Recebimento dos dados
primeiroNumero = int(input("Insira o primeiro valor:"))
segundoNumero = int(input("Insira o segundo valor:"))

#Tratando os dados e imprimindo o resultado
if primeiroNumero > segundoNumero:
    print("O número", primeiroNumero, "é maior que o número", segundoNumero)
else:
    print("O número", segundoNumero, "é maior que o número", primeiroNumero)

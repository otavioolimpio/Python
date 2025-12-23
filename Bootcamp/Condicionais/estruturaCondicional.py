MAIOR_IDADE = 18

idade = int(input("Digite sua idade: "))
if idade >= MAIOR_IDADE:
    if idade < 100:
        print("Você pode tirar a carteira de motorista.") # if aninhado
elif idade == MAIOR_IDADE - 1:
    print("Você poderá tirar a carteira de motorista no próximo ano.")
else:
    print("Você não pode tirar a carteira de motorista.")

# if ternário
mensagem = "Pode tirar a carteira de motorista." if idade >= MAIOR_IDADE else "Não pode tirar a carteira de motorista."
print(mensagem)
print("Fim do programa.")
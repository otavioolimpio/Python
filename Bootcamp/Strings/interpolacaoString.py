nome = "Otavio"
idade = 19
profissao = "Estudante"

# old format %
print("Nome: %s Idade: %d Profissão: %s" % (nome, idade, profissao)) # %s para string, %d para inteiros, %f para float

# format method
print("Nome: {} Idade: {} Profissão: {}".format(nome, idade, profissao)) # {} são placeholders
print("Nome: {0} Idade: {1} Profissão: {2}".format(nome, idade, profissao)) # pode-se usar índices
print("Olá, meu nome é {nome}, tenho {idade} anos e sou {profissao}".format(nome=nome, idade=idade, profissao=profissao)) # pode-se usar nomes
print(f"Olá, meu nome é {nome}, tenho {idade} anos e sou {profissao}") # f-strings (Python 3.6+)

PI = 3.14159
print("Valor de PI: %.2f" % PI) # formatando float com 2 casas decimais
print("Valor de PI: {:10.2f}".format(PI)) # formatando float com 2 casas decimais e largura mínima de 10
print(f"Valor de PI: {PI:.2f}") # formatando float com 2 casas decimais em f-string
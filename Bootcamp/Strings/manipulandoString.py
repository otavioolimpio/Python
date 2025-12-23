curso = "PyThOn"

print(curso.lower())  # Converte para minúsculas
print(curso.upper())  # Converte para maiúsculas    
print(curso.title())  # Converte para formato título
print(curso.capitalize())  # Converte a primeira letra para maiúscula

frase = "  Aprendendo Python  "
print(frase.strip())  # Remove espaços em branco no início e no fim 
print(frase.lstrip())  # Remove espaços em branco no início
print(frase.rstrip())  # Remove espaços em branco no fim
print(frase.replace("Python", "Java"))  # Substitui "Python" por "Java"
print(frase.split())  # Divide a frase em uma lista de palavras
print(frase.center(30, "-"))  # Centraliza a frase com preenchimento de '-'
print(".".join(["Aprendendo", "Python"]))  # Junta elementos com '.'
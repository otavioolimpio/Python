import csv
from pathlib import Path

ROOT_PATH = Path(__file__).parent

try:
    with open(ROOT_PATH / "Usuarios.csv", "w", encoding="utf-8", newline="") as arquivo_csv: # newline="" evita linhas em branco extras no Windows
        escritor_csv = csv.writer(arquivo_csv)
        escritor_csv.writerow(["Nome", "Idade", "Cidade"])
        escritor_csv.writerow(["Alice", 30, "São Paulo"])
        escritor_csv.writerow(["Bob", 25, "Rio de Janeiro"])
        escritor_csv.writerow(["Charlie", 35, "Belo Horizonte"])
except Exception as e:
    print(f"Erro ao escrever no arquivo CSV: {e}")

try:
    with open(ROOT_PATH / "Usuarios.csv", "r", encoding="utf-8") as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv)
        for linha in leitor_csv:
            print(linha)

    
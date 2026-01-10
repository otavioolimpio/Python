# Crie um quiz sobre as capitais dos países
# Cada ´pergunta deve ter 4 opções de resposta
# O usuário deve escolher a resposta correta

quiz = [
    {
        "pergunta": "Qual é a capital do Brasil?",
        "opcoes": ["São Paulo", "Rio de Janeiro", "Brasília", "Salvador"],
        "resposta": 2
    },
    {
        "pergunta": "Qual é a capital da França?",
        "opcoes": ["Lyon", "Marselha", "Paris", "Nice"],
        "resposta": 2
    },
    {
        "pergunta": "Qual é a capital da Alemanha?",
        "opcoes": ["Hamburgo", "Munique", "Berlim", "Frankfurt"],
        "resposta": 2
    }
]

def run_quiz():
    score = 0
    for q in quiz:
        print(q["pergunta"])
        for i, opcao in enumerate(q["opcoes"]):
            print(f"{i+1}. {opcao}")
        resposta = int(input("Escolha uma opção: ")) - 1
        if resposta == q["resposta"]:
            score += 1
            print("Resposta correta!")
        else:
            print("Resposta incorreta.")
    print(f"Você acertou {score} de {len(quiz)} perguntas.")

run_quiz()
import json
# salvar_pontuacao
def salvar_pontuacao(nome, pontos, file="pontuacoes.json"):
    try:
        with open(file, "r") as arquivo:
            pontuacoes = json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        pontuacoes = []

    pontuacoes.append({
        "nome": nome,
        "pontos": pontos
    })

    with open(file, "w") as arquivo:
        json.dump(pontuacoes, arquivo, indent=4)

# ler_pontuacoes
def ler_pontuacoes():
    pontuacoes = []
    try:
        with open("pontuacoes.txt", "r") as arquivo:
            for linha in arquivo:
                nome, pontos = linha.strip().split(",")
                pontuacoes.append((nome, int(pontos)))
    except FileNotFoundError:
        pass  
    return pontuacoes
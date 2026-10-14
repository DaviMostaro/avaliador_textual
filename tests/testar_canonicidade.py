from src.features.canonicidade import palavra_canonica, analisar_texto

palavras = [
    "cabeça",
    "canela",
    "janela",
    "luta",
    "sopa",
    "abajur",
    "lápis",
    "cansado",
    "asa",
    "alheio",
]

for palavra in palavras:
    resultado = palavra_canonica(palavra)
    print(palavra, "->", "Canônica" if resultado else "Não canônica")


print("\nAnálise de uma frase:")
texto = "A menina brincou no parque."
print(analisar_texto(texto))

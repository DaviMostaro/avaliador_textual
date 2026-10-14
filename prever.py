from src.models.persistence import carregar_modelo

modelo = carregar_modelo()

textos = [
    "O menino chutou a bola.",
    "A fotossíntese converte energia luminosa em energia química.",
    "A epistemologia investiga os fundamentos do conhecimento científico.",
]

previsoes = modelo.predict(textos)

for texto, classe in zip(textos, previsoes):
    print("\nTexto:", texto)
    print("Complexidade prevista:", classe)

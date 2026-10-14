from pathlib import Path
import re
from statistics import mean, median


dataset = Path("dataset_caed")


for pasta in dataset.iterdir():

    if not pasta.is_dir():
        continue

    frases_limpas = []

    arquivos = list(pasta.glob("*.txt"))

    for arquivo in arquivos:
        texto = arquivo.read_text(encoding="utf-8")

        frases = re.split(r"(?<=[.!?])\s+", texto)

        for frase in frases:
            frase = frase.strip()

            if frase:
                frases_limpas.append(frase)

    tamanhos = []

    for frase in frases_limpas:
        palavras = frase.split()
        quantidade_palavras = len(palavras)

        tamanhos.append(quantidade_palavras)

    faixas = {
        "1-2": 0,
        "3-5": 0,
        "6-10": 0,
        "11-20": 0,
        "21-30": 0,
        "31-50": 0,
        "51+": 0
    }


    for tamanho in tamanhos:

        if tamanho <= 2:
            faixas["1-2"] += 1

        elif tamanho <= 5:
            faixas["3-5"] += 1

        elif tamanho <= 10:
            faixas["6-10"] += 1

        elif tamanho <= 20:
            faixas["11-20"] += 1

        elif tamanho <= 30:
            faixas["21-30"] += 1

        elif tamanho <= 50:
            faixas["31-50"] += 1

        else:
            faixas["51+"] += 1


    # print(f"\nClasse: {pasta.name}")
    # print(f"Arquivos: {len(arquivos)}")
    # print(f"Frases: {len(frases_limpas)}")
    # print(f"Média de palavras por frase: {mean(tamanhos):.1f}")
    # print(f"Mediana: {median(tamanhos):.1f}")
    # print(f"Menor frase: {min(tamanhos)} palavras")
    # print(f"Maior frase: {max(tamanhos)} palavras")

    print(f"\nClasse: {pasta.name}")
    print(f"Arquivos: {len(arquivos)}")
    print(f"Frases: {len(frases_limpas)}")

    print("\nDistribuição das frases:")

    for faixa, quantidade in faixas.items():
        print(f"{faixa} palavras: {quantidade}")
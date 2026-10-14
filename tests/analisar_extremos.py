from pathlib import Path
import re


dataset = Path("dataset_caed")


for pasta in dataset.iterdir():

    if not pasta.is_dir():
        continue

    frases_pequenas = []
    frases_grandes = []

    arquivos = list(pasta.glob("*.txt"))

    for arquivo in arquivos:

        texto = arquivo.read_text(encoding="utf-8")

        frases = re.split(r"(?<=[.!?])\s+", texto)

        for frase in frases:

            frase = frase.strip()

            if not frase:
                continue

            quantidade_palavras = len(frase.split())

            if quantidade_palavras <= 2:
                frases_pequenas.append(frase)

            elif quantidade_palavras >= 51:
                frases_grandes.append(frase)


    print(f"\n{'=' * 50}")
    print(f"CLASSE: {pasta.name}")
    print(f"{'=' * 50}")

    print("\nFrases com 1-2 palavras:")

    for frase in frases_pequenas[:10]:
        print(f"- {frase}")


    print("\nFrases com 51+ palavras:")

    for frase in frases_grandes[:10]:
        print(f"- {frase}")
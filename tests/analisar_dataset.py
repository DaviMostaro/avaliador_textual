from pathlib import Path

dataset = Path("dataset_caed")

for pasta in dataset.iterdir():
    if pasta.is_dir():
        arquivos = list(pasta.glob("*.txt"))

        print(f"\nClasse: {pasta.name}")
        print(f"Arquivos: {len(arquivos)}")

        total_palavras = 0
        total_caracteres = 0
        total_paragrafos = 0

        for arquivo in arquivos:
            texto = arquivo.read_text(encoding="utf-8")

            total_caracteres += len(texto)
            total_palavras += len(texto.split())

            paragrafos = []

            linhas = texto.split("\n")

            for p in linhas:
                p = p.strip()

                if p:
                    paragrafos.append(p)

            total_paragrafos += len(paragrafos)

        print(f"Total de palavras: {total_palavras}")
        print(f"Média de palavras por arquivo: {total_palavras / len(arquivos):.1f}")
        print(f"Média de caracteres por arquivo: {total_caracteres / len(arquivos):.1f}")
        print(f"Média de parágrafos por arquivo: {total_paragrafos / len(arquivos):.1f}")
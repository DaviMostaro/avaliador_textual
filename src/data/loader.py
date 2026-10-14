from pathlib import Path

def carregar_arquivos(caminho_dataset):
    caminho_dataset = Path(caminho_dataset)

    classes = {
        "1_Ensino_Fundamental_I": "Ensino Fundamental I",
        "2_Ensino_Fundamental_II": "Ensino Fundamental II",
        "3_Ensino_Medio": "Ensino Médio",
        "4_Ensino_Superior": "Ensino Superior",
    }

    exemplos = []

    for nome_pasta, nome_classe in classes.items():
        pasta = caminho_dataset / nome_pasta

        for arquivo in pasta.rglob("*.txt"):
            texto = arquivo.read_text(encoding="utf-8")

            exemplo = {
                "texto": texto,
                "classe": nome_classe,
                "arquivo_id": str(arquivo.relative_to(caminho_dataset)),
            }

            exemplos.append(exemplo)

    return exemplos
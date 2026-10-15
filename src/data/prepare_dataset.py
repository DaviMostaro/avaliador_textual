from src.data.loader import carregar_arquivos

def preparar_exemplos(caminho_dataset):
    arquivos = carregar_arquivos(caminho_dataset)

    exemplos = []

    for indice_arquivo, arquivo in enumerate(arquivos):
        exemplo = {
            "texto": arquivo["texto"],
            "classe": arquivo["classe"],
            "arquivo_id": indice_arquivo,
        }

        exemplos.append(exemplo)

    return exemplos
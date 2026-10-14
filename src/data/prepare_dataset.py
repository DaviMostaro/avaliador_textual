from src.data.loader import carregar_arquivos
from src.data.preprocessing import separar_frases

def preparar_exemplos(caminho_dataset):
    arquivos = carregar_arquivos(caminho_dataset)

    exemplos = []

    for indice_arquivo, arquivo in enumerate(arquivos):
        texto = arquivo["texto"]
        classe = arquivo["classe"]

        frases = separar_frases(texto)

        for frase in frases:
            exemplo = {
                "texto": frase,
                "classe": classe,        
                "arquivo_id": indice_arquivo
            }

            exemplos.append(exemplo)

    return exemplos
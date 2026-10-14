from src.data.loader import carregar_arquivos
from src.data.split_dataset import separar_arquivos
from src.data.preprocessing import separar_frases

def extrair_frases(arquivos):
    exemplos = []

    for arquivo in arquivos:
        frases = separar_frases(arquivo["texto"])

        for frase in frases:
            exemplo = {
                "texto": frase,
                "classe": arquivo["classe"],
                "arquivo_id": arquivo["arquivo_id"],
            }

            exemplos.append(exemplo)

    return exemplos

def construir_datasets(caminho_dataset):
    arquivos = carregar_arquivos(caminho_dataset)

    treino_arquivos, validacao_arquivos, teste_arquivos = (
        separar_arquivos(arquivos)
    )

    treino = extrair_frases(treino_arquivos)
    validacao = extrair_frases(validacao_arquivos)
    teste = extrair_frases(teste_arquivos)

    return treino, validacao, teste
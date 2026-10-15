from src.data.loader import carregar_arquivos
from src.data.split_dataset import separar_arquivos

def construir_datasets(caminho_dataset):
    arquivos = carregar_arquivos(caminho_dataset)

    treino, validacao, teste = separar_arquivos(arquivos)

    return treino, validacao, teste
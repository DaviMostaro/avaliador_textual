from src.data.loader import carregar_arquivos
from src.data.split_dataset import separar_arquivos


arquivos = carregar_arquivos("dataset_caed")

treino, validacao, teste = separar_arquivos(arquivos)

print("Total:", len(arquivos))
print("Treino:", len(treino))
print("Validação:", len(validacao))
print("Teste:", len(teste))

print("\nDistribuição das classes no treino:")

contagens = {}

for arquivo in treino:
    classe = arquivo["classe"]

    if classe not in contagens:
        contagens[classe] = 0

    contagens[classe] += 1

for classe, quantidade in contagens.items():
    print(classe + ":", quantidade)
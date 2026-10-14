
from src.data.build_dataset import construir_datasets

treino, validacao, teste = construir_datasets("dataset_caed")

ids_treino = set()
ids_validacao = set()
ids_teste = set()

for exemplo in treino:
    ids_treino.add(exemplo["arquivo_id"])

for exemplo in validacao:
    ids_validacao.add(exemplo["arquivo_id"])

for exemplo in teste:
    ids_teste.add(exemplo["arquivo_id"])

print("Arquivos no treino:", len(ids_treino))
print("Arquivos na validação:", len(ids_validacao))
print("Arquivos no teste:", len(ids_teste))

print(
    "Treino e validação compartilham arquivos:",
    len(ids_treino & ids_validacao),
)

print(
    "Treino e teste compartilham arquivos:",
    len(ids_treino & ids_teste),
)

print(
    "Validação e teste compartilham arquivos:",
    len(ids_validacao & ids_teste),
)

print("Quantidade de frases:")
print("Treino:", len(treino))
print("Validação:", len(validacao))
print("Teste:", len(teste))

print("\nExemplo de treino:")
print(treino[0])

print("\nDistribuição das classes no treino:")

contagens = {}

for exemplo in treino:
    classe = exemplo["classe"]

    if classe not in contagens:
        contagens[classe] = 0

    contagens[classe] += 1

for classe, quantidade in contagens.items():
    print(classe + ":", quantidade)
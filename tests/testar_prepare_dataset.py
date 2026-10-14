from src.data.prepare_dataset import preparar_exemplos

exemplos = preparar_exemplos("dataset_caed")

print("Total de frases:", len(exemplos))

print("\nPrimeiro exemplo:")
print("Texto:", exemplos[0]["texto"])
print("Classe:", exemplos[0]["classe"])
print("Arquivo ID:", exemplos[0]["arquivo_id"])

print("\nQuantidade por classe:")

contagens = {}

for exemplo in exemplos:
    classe = exemplo["classe"]

    if classe not in contagens:
        contagens[classe] = 0

    contagens[classe] += 1

for classe, quantidade in contagens.items():
    print(classe + ":", quantidade)
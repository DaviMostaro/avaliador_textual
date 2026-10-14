from src.data.loader import carregar_arquivos


exemplos = carregar_arquivos("dataset_caed")

print("Total de arquivos:", len(exemplos))

print("\nPrimeiro exemplo:")
print("Classe:", exemplos[0]["classe"])
print("Texto:", exemplos[0]["texto"][:300])
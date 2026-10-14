from src.data.build_dataset import construir_datasets
from src.models.train import treinar_modelo
from src.models.persistence import salvar_modelo

treino, validacao, teste = construir_datasets("dataset_caed")

print("Treinando o modelo...")

modelo = treinar_modelo(treino)

print("Treinamento concluído!")

salvar_modelo(modelo)

frases_teste = [
    "A menina brincou no parque.",
    "A fotossíntese converte energia luminosa em energia química.",
    "A epistemologia investiga os fundamentos do conhecimento científico.",
    "O cachorro dormiu na sala.",
]

previsoes = modelo.predict(frases_teste)

print("\nPrevisões:")

for frase, classe in zip(frases_teste, previsoes):
    print("\nTexto:", frase)
    print("Classe prevista:", classe)
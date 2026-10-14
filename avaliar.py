from src.data.build_dataset import construir_datasets
from src.models.train import treinar_modelo
from src.evaluation.metrics import avaliar_modelo

treino, validacao, teste = construir_datasets("dataset_caed")

print("Treinando modelo...")
modelo = treinar_modelo(treino)

print("\nAvaliando no conjunto de validação...")
avaliar_modelo(modelo, validacao)
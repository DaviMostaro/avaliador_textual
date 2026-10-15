from src.evaluation.metrics import avaliar_modelo
from src.models.persistence import carregar_modelo
from src.data.build_dataset import construir_datasets

treino, validacao, teste = construir_datasets("dataset_caed")

modelo = carregar_modelo()

print("\nAvaliando no conjunto de validação...")
avaliar_modelo(modelo, validacao)
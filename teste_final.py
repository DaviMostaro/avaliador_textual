from src.evaluation.metrics import avaliar_modelo
from src.models.persistence import carregar_modelo
from src.data.build_dataset import construir_datasets

_, _, teste = construir_datasets("dataset_caed")

modelo = carregar_modelo()

print("\nAVALIAÇÃO FINAL NO CONJUNTO DE TESTE")
print("=" * 40)
avaliar_modelo(modelo, teste)

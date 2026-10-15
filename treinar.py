from pathlib import Path

import joblib

from src.data.build_dataset import construir_datasets
from src.models.train import treinar_modelo
from src.evaluation.metrics import avaliar_modelo

treino, validacao, teste = construir_datasets("dataset_caed")

print("Treinando regressão logística...")
modelo_logistica = treinar_modelo(treino, tipo="logistica")

print("\n=== REGRESSÃO LOGÍSTICA ===")
avaliar_modelo(modelo_logistica, validacao)

print("\nTreinando SVM...")
modelo_svm = treinar_modelo(treino, tipo="svm")

print("\n=== SVM ===")
avaliar_modelo(modelo_svm, validacao)

pasta_modelos = Path("modelos")
pasta_modelos.mkdir(parents=True, exist_ok=True)

caminho_modelo = pasta_modelos / "modelo_caed_svm.joblib"
joblib.dump(modelo_svm, caminho_modelo)

print(f"\nModelo SVM salvo em: {caminho_modelo}")

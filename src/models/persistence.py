from pathlib import Path
import joblib

CAMINHO_MODELO = Path("modelos/modelo_caed_svm.joblib")

def salvar_modelo(modelo):
    CAMINHO_MODELO.parent.mkdir(parents=True, exist_ok=True)

    joblib.dump(modelo, CAMINHO_MODELO)

    print(f"Modelo salvo em: {CAMINHO_MODELO}")

def carregar_modelo():
    if not CAMINHO_MODELO.exists():
        raise FileNotFoundError(
            "Modelo não encontrado. Execute treinar.py primeiro."
        )

    modelo = joblib.load(CAMINHO_MODELO)

    return modelo
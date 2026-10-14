import numpy as np
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import FunctionTransformer
from sklearn.linear_model import LogisticRegression
from src.features.canonicidade import analisar_texto

def extrair_caracteristicas_canonicas(textos):
    caracteristicas = []

    for texto in textos:
        resultado = analisar_texto(texto)

        proporcao = resultado["proporcao_canonicas"]
        caracteristicas.append([proporcao])

    return np.array(caracteristicas)
    
def treinar_modelo(exemplos):
    textos = []
    classes = []

    for exemplo in exemplos:
        textos.append(exemplo["texto"])
        classes.append(exemplo["classe"])

    extrator_caracteristicas = FeatureUnion([
        (
            "tfidf",
            TfidfVectorizer(
                lowercase=True,
                ngram_range=(1, 2),
                min_df = 2,
                max_features=50000,
            ),
        ),
        (
            "canonicidade",
            FunctionTransformer(
                extrair_caracteristicas_canonicas,
                validate=False
            ),
        ),
    ])

    modelo = Pipeline([
        (
            "caracteristicas",
            extrator_caracteristicas
        ),
        (
            "classificador",
            LogisticRegression(
                max_iter=1000,
                class_weight="balanced",
                random_state=42,
            ),
        ),
    ])

    modelo.fit(textos, classes)

    return modelo
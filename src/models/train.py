import numpy as np
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import FunctionTransformer, StandardScaler
from sklearn.linear_model import LogisticRegression
from src.features.canonicidade import analisar_texto
from sklearn.svm import LinearSVC
from src.features.caracteristicas_linguisticas import (
    analisar_caracteristicas_linguisticas,
)
from src.features.caracteristicas_sintaticas import (
    extrair_caracteristicas_sintaticas,
)
from src.features.raridade_lexical import RaridadeLexical

def extrair_caracteristicas_canonicas(textos):
    caracteristicas = []

    for texto in textos:
        resultado = analisar_texto(texto)

        proporcao = resultado["proporcao_canonicas"]
        caracteristicas.append([proporcao])

    return np.array(caracteristicas)

def extrair_caracteristicas_linguisticas(textos):
    caracteristicas = []

    for texto in textos:
        resultado = analisar_caracteristicas_linguisticas(texto)

        linha = [
            np.log1p(resultado["total_palavras"]),
            resultado["comprimento_medio_palavra"],
            resultado["proporcao_palavras_longas"],
            resultado["diversidade_lexical"],
        ]

        caracteristicas.append(linha)
        
    return np.array(caracteristicas, dtype=float)

def treinar_modelo(exemplos, tipo="svm"):
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
        (
            "linguisticas",
            Pipeline([
                (
                    "extracao",
                    FunctionTransformer(
                        extrair_caracteristicas_linguisticas,
                        validate=False,
                    ),
                ),
                ("padronização", StandardScaler())
            ])
        ),
        (
            "sintaticas",
            Pipeline([
                (
                    "extracao",
                    FunctionTransformer(
                        extrair_caracteristicas_sintaticas,
                        validate=False,
                    ),
                ),
                ("padronização", StandardScaler()),
            ]),
        ),
        (
            "raridade_lexical", 
            Pipeline([
                ("extracao", RaridadeLexical()),
                ("padronização", StandardScaler()),
            ]),
        ),
    ])

    if tipo == "logistica":
        classificador = LogisticRegression(
            max_iter=1000,
            class_weight="balanced",
            random_state=42,
        )
    elif tipo == "svm":
        classificador = LinearSVC(
            class_weight="balanced",
            random_state=42,
            max_iter=5000,
        )
    else:
        raise ValueError("Tipo deve ser 'logistica' ou 'svm'.")

    modelo = Pipeline([
        ("caracteristicas", extrator_caracteristicas),
        ("classificador", classificador),
    ])
    
    modelo.fit(textos, classes)

    return modelo
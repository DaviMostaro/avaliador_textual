import re
import math
import numpy as np

from sklearn.base import BaseEstimator, TransformerMixin

class RaridadeLexical(BaseEstimator, TransformerMixin):
    def __init__(self, proporcao_limite=0.01):
        self.proporcao_limite = proporcao_limite

    def extrair_palavras(self, texto):
        return re.findall(
            r"\b[a-záàâãéêíóôõúüç]+\b",
            texto.lower()
        )

    def fit(self, X, y = None):
        frequencias_documentos = {}
        total_documentos = len(X)

        for texto in X:
            palavras = set(self.extrair_palavras(texto))

            for palavra in palavras:
                frequencias_documentos[palavra] = (
                    frequencias_documentos.get(palavra, 0) + 1
                )

        self.frequencias_documentos_ = frequencias_documentos

        self.limite_raridade_ = max(
            2,
            math.ceil(total_documentos * self.proporcao_limite)
        )

        return self

    def transform(self, X):
        caracteristicas = []

        for texto in X:
            palavras = self.extrair_palavras(texto)

            if not palavras:
                caracteristicas.append([0, 0])
                continue

            palavras_raras = sum(
                1
                for palavra in palavras
                if self.frequencias_documentos_.get(palavra, 0)
                <= self.limite_raridade_
            )

            proporcao_raras = palavras_raras / len(palavras)

            caracteristicas.append([proporcao_raras])

        return np.array(caracteristicas, dtype=float)
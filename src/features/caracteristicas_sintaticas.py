import numpy as np
import spacy

nlp = spacy.load("pt_core_news_sm")

DEPENDENCIAS_SUBORDINADAS = {
    "acl",
    "acl:relcl",
    "advcl",
    "ccomp",
    "csubj",
    "csubj:pass",
    "xcomp",
}

def calcular_profundidade(token):
    profundidade = 0
    atual = token

    while atual.head != atual:
        profundidade += 1
        atual = atual.head

    return profundidade

def analisar_caracteristicas_sintaticas(texto):
    doc = nlp(texto)

    palavras = [
        token for token in doc
        if not token.is_punct and not token.is_space
    ]

    frases = list(doc.sents)

    total_palavras = len(palavras)
    total_frases = len(frases)

    if total_palavras == 0:
        return {
            "media_palavras_por_frase": 0,
            "proporcao_subordinacoes": 0,
            "proporcao_apostos": 0,
            "profundidade_sintatica_media": 0,
            "proporcao_verbos": 0,
        }

    total_subordinacoes = sum(
        1 for token in palavras
        if token.dep_ in DEPENDENCIAS_SUBORDINADAS
    )

    total_apostos = sum(
        1 for token in palavras
        if token.dep_ == "appos"
    )

    total_verbos = sum(
        1 for token in palavras
        if token.pos == "VERB"
    )

    profundidades = [
        calcular_profundidade(token)
        for token in palavras
    ]

    media_palavras_por_frase = (
        total_palavras / max(total_frases, 1)
    )

    return {
        "media_palavras_por_frase": media_palavras_por_frase,
        "proporcao_subordinacoes": (
            total_subordinacoes / max(total_frases, 1)
        ),
        "proporcao_apostos": total_apostos / total_palavras,
        "profundidade_sintatica_media": (
            sum(profundidades) / total_palavras
        ),
        "proporcao_verbos": total_verbos / total_palavras,
    }

def extrair_caracteristicas_sintaticas(textos):
    caracteristicas = []

    for texto in textos:
        resultado = analisar_caracteristicas_sintaticas(texto)

        linha = [
            resultado["media_palavras_por_frase"],
            resultado["proporcao_subordinacoes"],
            resultado["proporcao_apostos"],
            resultado["profundidade_sintatica_media"],
            resultado["proporcao_verbos"],
        ]

        caracteristicas.append(linha)

    return np.array(caracteristicas, dtype=float)
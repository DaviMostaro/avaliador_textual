import re

def analisar_caracteristicas_linguisticas(texto):
    palavras = re.findall(r"[a-zA-ZÀ-ÿ]+", texto)
    total = len(palavras)

    if total == 0:
        return {
            "total_palavras": 0,
            "comprimento_medio_palavra": 0,
            "proporcao_palavras_longas": 0,
            "diversidade_lexical": 0,
        }

    comprimentos = [len(palavra) for palavra in palavras]

    palavras_distintas = set(
        palavra.lower() for palavra in palavras
    )

    return {
        "total_palavras": total,
        "comprimento_medio_palavra": sum(comprimentos) / total,
        "proporcao_palavras_longas": sum(
            1 for tamanho in comprimentos if tamanho >= 7
        ) / total,
        "diversidade_lexical": len(palavras_distintas) / total
    }
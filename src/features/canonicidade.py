import re
import unicodedata
import pyphen

separador = pyphen.Pyphen(lang='pt_BR')

def normalizar_silaba(silaba):
    silaba = silaba.lower()
    silaba = unicodedata.normalize("NFD", silaba)
    silaba = "".join(
        letra for letra in silaba
        if unicodedata.category(letra) != "Mn"
    )

    silaba = re.sub(r"ch|lh|nh|rr|ss", "C", silaba)

    silaba = re.sub(r"qu(?=[ei])", "C", silaba)
    silaba = re.sub(r"gu(?=[ei])", "C", silaba)

    return silaba

def palavra_canonica(palavra):
    palavra = palavra.lower()

    silabas = separador.inserted(palavra).split("-")

    for silaba in silabas:
        silaba = normalizar_silaba(silaba)

        if not re.fullmatch(r"[^aeiou][aeiou]", silaba):
            return False

    return True

def analisar_texto(texto):
    palavras = re.findall(r"[a-zA-ZÀ-ÿ]+", texto)

    total = len(palavras)
    canonicas = 0
    nao_canonicas = 0

    for palavra in palavras:
        if palavra_canonica(palavra):
            canonicas += 1
        else:
            nao_canonicas += 1

    proporcao_canonicas = canonicas / total if total > 0 else 0
    proporcao_nao_canonicas = nao_canonicas / total if total > 0 else 0

    return {
        "total_palavras": total,
        "palavras_canonicas": canonicas,
        "palavras_nao_canonicas": nao_canonicas,
        "proporcao_canonicas": proporcao_canonicas,
        "proporcao_nao_canonicas": proporcao_nao_canonicas
    }
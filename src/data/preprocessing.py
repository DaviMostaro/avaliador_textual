import re

def separar_frases(texto):
    frases = re.split(r"(?<=[.!?])\s+", texto)

    frases_limpas = []

    for frase in frases:
        frase = frase.strip()

        if frase: 
            frases_limpas.append(frase)


    return frases_limpas
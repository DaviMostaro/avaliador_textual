from src.data.preprocessing import separar_frases


texto = "A menina correu. O menino caminhou! Depois, foram para casa."

frases = separar_frases(texto)

print(frases)
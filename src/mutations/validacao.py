def validar_sinonimo(texto_original, resultado):
    campos = [
        "texto_modificado",
        "palavra_original",
        "palavra_substituta",
    ]

    for campo in campos:
        if campo not in resultado:
            return False

    texto_modificado = resultado["texto_modificado"]

    if not isinstance(texto_modificado, str):
        return False

    if not texto_modificado.strip():
        return False

    if texto_modificado == texto_original:
        return (
            resultado["palavra_original"] is None
            and resultado["palavra_substituta"] is None
        )

    if not resultado["palavra_original"]:
        return False

    if not resultado["palavra_substituta"]:
        return False

    return True

def validar_genero(texto_original, resultado):
    campos = [
        "texto_modificado",
        "genero_original",
        "genero_novo",
    ]

    for campo in campos:
        if campo not in resultado:
            return False

    texto_modificado = resultado["texto_modificado"]

    if not isinstance(texto_modificado, str):
        return False

    if not texto_modificado.strip():
        return False

    if texto_modificado == texto_original:
        return (
            resultado["genero_original"] is None
            and resultado["genero_novo"] is None
        )

    if not resultado["genero_original"]:
        return False

    if not resultado["genero_novo"]:
        return False

    return True

def validar_parafrase(texto_original, resultado):
    if "texto_modificado" not in resultado:
        return False

    texto_modificado = resultado["texto_modificado"]

    if not isinstance(texto_modificado, str):
        return False

    if not texto_modificado.strip():
        return False

    return True
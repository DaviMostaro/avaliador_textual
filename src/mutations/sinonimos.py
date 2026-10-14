import json

from src.mutations.cliente_ia import gerar_resposta
from src.mutations.validacao import validar_sinonimo

def substituir_palavra(texto, tipo="sinonimo"):
    if tipo not in ("sinonimo", "antonimo"):
        raise ValueError(
            "O tipo deve ser 'sinonimo' ou 'antonimo'."
        )

    instrucao = f"""
        Você é um assistente especializado em língua portuguesa.

        Receba o texto abaixo e realize uma mutação do tipo: {tipo}.

        Regras:
        - Substitua apenas UMA palavra por um {tipo}.
        - Escolha uma palavra que possa ser substituída sem tornar a frase
        gramaticalmente incorreta.
        - Considere o contexto para escolher uma substituição adequada.
        - Preserve o restante do texto, inclusive a pontuação.
        - Se não houver uma substituição adequada, retorne o texto original.
        - Não invente palavras nem acrescente explicações.
        - Retorne somente um JSON válido com os campos:
        "texto_modificado", "palavra_original", "palavra_substituta".

        Se nenhuma substituição for possível, use null nos dois campos
        de palavra e mantenha o texto original.

        Texto: {json.dumps(texto, ensure_ascii=False)}
    """

    resposta = gerar_resposta(instrucao)

    resultado = json.loads(resposta.text)

    if not validar_sinonimo(texto, resultado):
        raise ValueError("A API retornou uma mutação inválida.")

    texto_modificado = resultado["texto_modificado"]

    return {
        "texto_original": texto,
        "texto_modificado": texto_modificado,
        "palavra_original": resultado["palavra_original"],
        "palavra_substituta": resultado["palavra_substituta"],
        "tipo": tipo,
        "modificado": texto_modificado != texto,
    }
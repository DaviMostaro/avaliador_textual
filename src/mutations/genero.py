import json

from src.mutations.cliente_ia import gerar_resposta
from src.mutations.validacao import validar_genero

def alterar_genero(texto):
    instrucao = f"""
        Você é um assistente especializado em língua portuguesa.

        Altere o gênero gramatical de uma pessoa ou personagem no texto.

        Regras:
        - Altere o gênero de apenas uma pessoa ou personagem.
        - Ajuste artigos, substantivos, adjetivos e outras palavras
        necessárias para manter a concordância gramatical.
        - Preserve o sentido geral da situação descrita.
        - Preserve o restante do texto sempre que possível.
        - Não altere o gênero de objetos ou elementos sem gênero humano.
        - Se não houver uma alteração adequada, mantenha o texto original.
        - Não acrescente explicações.
        - Retorne somente JSON válido com os campos:
        "texto_modificado", "genero_original", "genero_novo".

        Se nenhuma alteração for possível, mantenha o texto original
        e use null nos campos de gênero.

        Texto: {json.dumps(texto, ensure_ascii=False)}
    """

    resposta = gerar_resposta(instrucao)

    resultado = json.loads(resposta.text)

    if not validar_genero(texto, resultado):
        raise ValueError("A API retornou uma mutação de genero inválida.")

    texto_modificado = resultado.get("texto_modificado")

    if not isinstance(texto_modificado, str) or not texto_modificado.strip():
        raise ValueError("A API retornou um texto inválido.")

    genero_original = resultado.get("genero_original")
    genero_novo = resultado.get("genero_novo")

    if texto_modificado == texto:
        genero_original = None
        genero_novo = None
    elif not genero_original or not genero_novo:
        raise ValueError(
            "A API alterou o texto, mas não informou os gêneros."
        )

    return {
        "texto_original": texto,
        "texto_modificado": texto_modificado,
        "genero_original": genero_original,
        "genero_novo": genero_novo,
        "modificado": texto_modificado != texto,
    }
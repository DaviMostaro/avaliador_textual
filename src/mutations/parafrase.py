import json

from src.mutations.cliente_ia import gerar_resposta
from src.mutations.validacao import validar_parafrase

def gerar_parafrase(texto):
    instrucao = f"""
        Você é um especialista em língua portuguesa.

        Reescreva o texto fornecido como uma paráfrase.

        Regras:
        - Preserve o sentido original do texto.
        - Modifique a estrutura da frase ou a ordem das palavras.
        - Mantenha as informações, os fatos e as relações entre as ideias.
        - Não acrescente informações novas.
        - Preserve a língua portuguesa e a correção gramatical.
        - Se não for possível produzir uma paráfrase adequada,
        mantenha o texto original.
        - Não acrescente explicações.
        - Retorne somente JSON válido com o campo:
        "texto_modificado".

        Texto original: {json.dumps(texto, ensure_ascii=False)}
    """

    resposta = gerar_resposta(instrucao)

    resultado = json.loads(resposta.text)

    if not validar_parafrase(texto, resultado):
        raise ValueError("A API retornou uma paráfrase inválida.")

    texto_modificado = resultado["texto_modificado"]

    return {
        "texto_original": texto,
        "texto_modificado": texto_modificado,
        "modificado": texto_modificado != texto,
    }
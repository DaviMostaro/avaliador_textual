import json

from src.mutations.cliente_ia import gerar_resposta
from src.mutations.validacao import validar_parafrase

def gerar_parafrase(texto):
    instrucao = f"""
        Você é um especialista em língua portuguesa.

        Reescreva o texto fornecido como uma paráfrase completa.

        Regras:
        - Parafraseie o texto inteiro, modificando a estrutura das frases,
        a ordem das palavras e as construções linguísticas sempre que
        isso for adequado.
        - Preserve o sentido original do texto.
        - Mantenha as informações, os fatos e as relações entre as ideias.
        - Não acrescente informações novas nem omita informações relevantes.
        - Preserve a sequência lógica do texto e a coerência entre as frases.
        - Preserve a língua portuguesa e a correção gramatical.
        - Mantenha aproximadamente a mesma extensão do texto original.
        - Não tente aumentar nem reduzir deliberadamente a complexidade
        linguística do texto.
        - Se não for possível produzir uma paráfrase adequada, mantenha
        o texto original.
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
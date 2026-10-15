import json

from src.mutations.cliente_ia import gerar_resposta
from src.mutations.validacao import validar_sinonimo

def substituir_palavra(texto, tipo="sinonimo"):
    if tipo not in ("sinonimo", "antonimo"):
        raise ValueError(
            "O tipo deve ser 'sinonimo' ou 'antonimo'."
        )

    instrucao = f"""
        Receba o texto abaixo e realize uma mutação do tipo: {tipo}.

        Regras:
        - Substitua palavras por {tipo} em várias frases do texto,
        sempre que houver substituições adequadas.
        - Procure substituir, preferencialmente, uma palavra por frase,
        mas não force alterações quando não houver uma opção adequada.
        - Escolha palavras cuja substituição seja apropriada ao contexto
        e mantenha a correção gramatical.
        - Se o tipo for sinônimo, preserve tanto quanto possível
        o sentido original das frases.
        - Se o tipo for antônimo, produza oposições de sentido coerentes
        com o contexto.
        - Preserve o restante do texto, inclusive a pontuação e a estrutura,
        exceto pelas alterações necessárias.
        - Não invente palavras nem acrescente explicações.
        - Se nenhuma substituição adequada for possível, retorne
        o texto original.
        - Retorne somente JSON válido com os campos:
        "texto_modificado", "palavra_original", "palavra_substituta".

        Os campos "palavra_original" e "palavra_substituta" devem ser
        listas contendo os pares de palavras substituídas, na mesma ordem.
        Se nenhuma substituição for possível, use null nos dois campos
        e mantenha o texto original.

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
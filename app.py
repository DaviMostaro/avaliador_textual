import streamlit as st

from src.models.persistence import carregar_modelo
from src.mutations.sinonimos import substituir_palavra
from src.mutations.genero import alterar_genero
from src.mutations.parafrase import gerar_parafrase

st.set_page_config(
    page_title="Avaliador de Complexidade Textual",
    page_icon="📚",
    layout="centered",
)

@st.cache_resource
def obter_modelo():
    return carregar_modelo()

modelo = obter_modelo()

st.title("Avaliador de Complexidade Textual")

st.write(
    "Digite um texto para avaliar sua complexidade "
    "segundo os quatro níveis de ensino."
)

texto = st.text_area(
    "Texto para avaliação",
    placeholder="Digite ou cole seu texto aqui...",
    height=180,
)

if st.button("Avaliar texto", type="primary"):
    if not texto.strip():
        st.warning("Digite um texto antes de avaliar.")
    else: 
        st.session_state["texto_original"] = texto
        st.session_state["classe_original"] = modelo.predict([texto])[0]

        for chave in [
            "texto_modificado",
            "mutacoes_aplicadas",
            "classe_modificada",
        ]:
            st.session_state.pop(chave, None)

if "classe_original" in st.session_state:
    st.subheader("Resultado da avaliação")

    st.write("**Texto original:**")
    st.write(st.session_state["texto_original"])

    st.write("**Complexidade prevista:**")
    st.success(str(st.session_state["classe_original"]))   

    st.divider()

    st.subheader("Escolha as mutações")

    usar_sinonimo = st.checkbox("Substituir uma palavra por sinônimo") 
    usar_antonimo = st.checkbox("Substituir uma palavra por antônimo")
    usar_genero = st.checkbox("Alterar gênero gramatical")
    usar_parafrase = st.checkbox("Parafrasear texto")

    if st.button("Gerar mutações", type="primary"):
        mutacoes_escolhidas = [
            usar_sinonimo,
            usar_antonimo,
            usar_genero,
            usar_parafrase
        ]

        if not any(mutacoes_escolhidas):
            st.warning("Selecione pelo menos uma mutação.")
        else:
            texto_atual = st.session_state["texto_original"]
            mutacoes_aplicadas = []

            try:
                if usar_sinonimo:
                    resultado = substituir_palavra(
                        texto_atual,
                        tipo="sinonimo",
                    )

                    texto_atual = resultado["texto_modificado"]

                    mutacoes_aplicadas.append({
                        "nome": "Sinônimo",
                        "resultado": resultado,
                    })

                if usar_antonimo:
                    resultado = substituir_palavra(
                        texto_atual,
                        tipo="antonimo",
                    )
                
                    texto_atual = resultado["texto_modificado"]
                
                    mutacoes_aplicadas.append({
                        "nome": "Antônimo",
                        "resultado": resultado,
                    })

                if usar_genero:
                    resultado = alterar_genero(
                        texto_atual
                    )

                    texto_atual = resultado["texto_modificado"]

                    mutacoes_aplicadas.append({
                        "nome": "Alteração de gênero",
                        "resultado": resultado,
                    })

                if usar_parafrase: 
                    resultado = gerar_parafrase(
                        texto_atual
                    )

                    texto_atual = resultado["texto_modificado"]

                    mutacoes_aplicadas.append({
                        "nome": "Paráfrase",
                        "resultado": resultado,
                    })

                st.session_state["texto_modificado"] = texto_atual
                st.session_state["mutacoes_aplicadas"] = mutacoes_aplicadas

                st.session_state.pop("classe_modificada", None)

            except Exception as erro:
                st.error(f"Não foi possível gerar as mutações: {erro}")

                st.session_state.pop("texto_modificado", None)
                st.session_state.pop("mutacoes_aplicadas", None)
                st.session_state.pop("classe_modificada", None)

    if "texto_modificado" in st.session_state:
        st.subheader("Texto modificado")

        st.write(st.session_state["texto_modificado"])

        st.write("**Resultado de cada mutação:**")

        for item in st.session_state["mutacoes_aplicadas"]:
            resultado = item["resultado"]

            if resultado["modificado"]:
                st.success(f'{item["nome"]}: aplicada')
            else:
                st.info(
                    f'{item["nome"]}: nenhuma alteração realizada'
                )

        if st.button("Classificar texto modificado"):
            texto_modificado = st.session_state["texto_modificado"]

            classe_modificada = modelo.predict([texto_modificado])[0]

            st.session_state["classe_modificada"] = classe_modificada

    if "classe_modificada" in st.session_state:
        st.divider()
        st.subheader("Comparação final")

        classe_original = st.session_state["classe_original"]
        classe_modificada = st.session_state["classe_modificada"]

        col1, col2 = st.columns(2)

        with col1:
            st.write("**Texto original**")
            st.info(str(classe_original))

        with col2:
            st.write("**Texto modificado**")
            st.info(str(classe_modificada))

        if classe_original == classe_modificada:
            st.success(
                "A classificação permaneceu no mesmo nível."
            )
        else: 
            st.warning(
                "A classificação mudou após as mutações."
            )

    st.divider()

    if st.button("Começar novamente"):
        for chave in [
            "texto_original",
            "classe_original",
            "texto_modificado",
            "mutacoes_aplicadas",
            "classe_modificada",
        ]:
            st.session_state.pop(chave, None)

        st.rerun()        

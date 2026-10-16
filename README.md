## Pré-requisitos

| Python | 3.12, 3.13 ou 3.14 (desenvolvido e testado com **3.14.4**) |
| Chave de API do Google Gemini | Obtenha em [https://aistudio.google.com/apikey](https://aistudio.google.com/apikey) |
| Sistema operacional | Windows, Linux ou macOS |

> **Importante:** a chave `GEMINI_API_KEY` é obrigatória até para apenas abrir a aplicação, pois é validada no carregamento do módulo de mutações (`src/mutations/cliente_ia.py`).

---

## Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/DaviMostaro/avaliador_textual.git
cd avaliador_textual
```

### 2. Crie e ative um ambiente virtual

**Windows (PowerShell):**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**Linux / macOS:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Baixe o modelo de português do spaCy

```bash
python -m spacy download pt_core_news_sm
```

---

## Configuração

Crie o arquivo `.env` na raiz do projeto a partir do modelo:

**Windows (PowerShell):**

```powershell
Copy-Item .env.example .env
```

**Linux / macOS:**

```bash
cp .env.example .env
```

Edite o `.env` e cole sua chave da API do Gemini:

```
GEMINI_API_KEY=sua_chave_aqui
```

## Executando a aplicação

Na raiz do projeto (com o ambiente virtual ativado):

```bash
streamlit run app.py
```

A aplicação abrirá no navegador em **http://localhost:8501**.

### Como usar

1. Digite ou cole um texto no campo **"Texto para avaliação"** e clique em **"Avaliar texto"**.
2. Veja o **texto original** e a **complexidade prevista**.
3. Marque as **mutações** desejadas (sinônimo, antônimo, gênero gramatical, paráfrase) e clique em **"Gerar mutações"**. *(Estas etapas consomem cota da API Gemini.)*
4. Clique em **"Classificar texto modificado"** para reavaliar o texto mutado.
5. A **"Comparação final"** mostra lado a lado a classificação do texto original e do texto modificado, indicando se o nível mudou.
6. Use **"Começar novamente"** para reiniciar.

> Execute os comandos sempre a partir da **raiz do projeto** — os caminhos dos modelos e do dataset são relativos.

O modelo treinado (`modelos/modelo_caed_svm.joblib`) já vem versionado no repositório, então **não é necessário treinar nada para usar a aplicação**.

## Estrutura do projeto

```
avaliador_textual/
├── app.py                     # Interface web (Streamlit) — entrypoint principal
├── treinar.py                 # Treino dos modelos (logística + SVM)
├── avaliar.py                 # Avaliação do modelo na validação
├── teste_final.py             # Avaliação final no conjunto de teste
├── prever.py                  # Inferência de exemplo
├── requirements.txt           # Dependências do projeto
├── .env.example               # Modelo de variável de ambiente
├── modelos/
│   └── modelo_caed_svm.joblib # Modelo SVM já treinado (em uso)
├── src/
│   ├── data/                  # Carga e separação do dataset
│   ├── features/              # Features: TF-IDF, canonicidade, linguísticas,
│   │                          #   sintáticas (spaCy) e raridade lexical
│   ├── models/                # Pipeline de treino (sklearn) e persistência
│   ├── evaluation/            # Métricas (acurácia, macro-F1, matriz de confusão)
│   └── mutations/             # Mutações via IA (Gemini): sinônimo, antônimo,
│                              #   gênero, paráfrase e validação das respostas
└── tests/                     # Scripts manuais de verificação (ver abaixo)
```


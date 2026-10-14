import os
import httpx
from dotenv import load_dotenv
from google import genai
from google.genai import errors, types

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError(
        "A chave GEMINI_API_KEY não foi encontrada no arquivo .env"
    )

cliente = genai.Client(
    api_key=API_KEY,
    http_options=types.HttpOptions(
        timeout=10000,
        retry_options=types.HttpRetryOptions(attempts=1),
    ),
)

MODELOS = [
    "gemini-3.8-flash",
    "gemini-3.5-flash-lite",
    "gemini-3.1-flash-lite",
    "gemini-3-flash-preview",
]


def gerar_resposta(instrucao):
    for modelo in MODELOS:
        try:
            print(f"Tentando modelo: {modelo}")

            resposta = cliente.models.generate_content(
                model=modelo,
                contents=instrucao,
                config={
                    "response_mime_type": "application/json",
                    "temperature": 0.2,
                },
            )

            print(f"Modelo utilizado: {modelo}")
            return resposta

        except httpx.TimeoutException:
            print(
                f"Modelo {modelo} excedeu o tempo limite de resposta. "
                "Tentando o próximo..."
            )
            continue

        except errors.APIError as erro:
            if erro.code in (404, 429, 500, 502, 503, 504):
                print(
                    f"Modelo {modelo} indisponível "
                    f"(erro {erro.code}). Tentando o próximo..."
                )
                continue

            raise

    raise RuntimeError(
        "Todos os modelos falharam. Tente novamente mais tarde."
    )

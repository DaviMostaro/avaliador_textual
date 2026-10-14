from src.mutations.parafrase import gerar_parafrase

texto = "O texto foi lido pelo aluno."

resultado = gerar_parafrase(texto)

print("Texto original:")
print(resultado["texto_original"])

print("\nParáfrase:")
print(resultado["texto_modificado"])

print("\nHouve alteração?")
print(resultado["modificado"])

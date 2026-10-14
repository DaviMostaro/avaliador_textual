from src.mutations.genero import alterar_genero

texto = "A cantora era famosa."

resultado = alterar_genero(texto)

print("Texto original:")
print(resultado["texto_original"])

print("\nTexto modificado:")
print(resultado["texto_modificado"])

print("\nGênero original:")
print(resultado["genero_original"])

print("\nNovo gênero:")
print(resultado["genero_novo"])

print("\nHouve alteração?")
print(resultado["modificado"])

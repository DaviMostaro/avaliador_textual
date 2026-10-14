from src.mutations.sinonimos import substituir_palavra

texto = "A menina está feliz porque ganhou um presente."

print("Texto original:")
print(texto)

print("\nMutação com sinônimo:")
resultado_sinonimo = substituir_palavra(texto, "sinonimo")
print(resultado_sinonimo)

print("\nMutação com antônimo:")
resultado_antonimo = substituir_palavra(texto, "antonimo")
print(resultado_antonimo)

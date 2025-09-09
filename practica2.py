
texto = "Programar en Python es divertido"

# Convertimos todo a minúsculas para no preocuparnos por mayúsculas/minúsculas
texto = texto.lower()

vocales = "aeiou"
contador = 0

for letra in texto:
    if letra in vocales:
        contador += 1

print("La cantidad de vocales es:", contador)

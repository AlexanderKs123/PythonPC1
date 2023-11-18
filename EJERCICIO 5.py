# Solicitamos al usuario la cantidad de shows musicales vistos
numero_shows = int(input("Ingrese el numero de shows musicales que ha visto en el último año: "))

# Verificamos si ha visto más de 3 shows
Ha_visto_mas_de_3 = numero_shows > 3

# Mostrar el resultado
print(f"¿Ha visto más de 3 shows musicales? {Ha_visto_mas_de_3}")
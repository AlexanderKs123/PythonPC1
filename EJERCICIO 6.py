edad_cliente = int(input("Ingrese la edad del cliente: "))

if edad_cliente < 4:
    precio_entrada = 0  # Gratis para menores de 4 años
elif 4 <= edad_cliente <= 18:
    precio_entrada = 5  # $5 para edades entre 4 y 18 años
else:
    precio_entrada = 10  # $10 para mayores de 18 años

print(f"El precio de la entrada es: ${precio_entrada}")
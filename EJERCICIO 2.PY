# Solicitamos el costo de la comida al usuario
costo_comida = float(input("Ingrese el costo de la comida: $"))

# Solicitamos el porcentaje de propina deseado
porcentaje_propina = float(input("Ingrese el porcentaje de propina que desea dejar (%): "))

# Calculamos la cantidad de dinero a dejar como propina
propina = costo_comida * (porcentaje_propina / 100)

# Mostramos la cantidad de dinero a dejar como propina
print(f"La propina a dejar es: ${propina:.2f}")
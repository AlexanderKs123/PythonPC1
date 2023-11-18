# Definimos el peso de los payasos y muñecas
peso_payaso = 112  # en gramos
peso_muneca = 75   # en gramos

# Solicitamos al usuario el número de payasos y muñecas vendidos
num_payasos = int(input("Ingrese el número de payasos vendidos: "))
num_munecas = int(input("Ingrese el número de muñecas vendidas: "))

# Calculamos el peso total del paquete
peso_total = (num_payasos * peso_payaso) + (num_munecas * peso_muneca)

# Mostramos el peso total del paquete
print(f"El peso total del paquete es: {peso_total} gramos")
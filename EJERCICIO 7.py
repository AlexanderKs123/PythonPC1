
numero_1 = float(input("Ingresamos el primer número: "))
numero_2 = float(input("Ingresamos el segundo número: "))

# Menú de opciones
print("Menú:")
print("1. Imprime la suma de los dos números")
print("2. Imprime la resta (primer número menos segundo número)")
print("3. Imprime la multiplicación de los dos números")

opcion = input("Ingresamos el número de la opción deseada (1, 2, o 3): ")

# Realizamos la operación correspondiente según la opción seleccionada
if opcion == '1':
    resultado = numero_1 + numero_2
    print(f"La suma de {numero_1} y {numero_2} es: {resultado}")
elif opcion == '2':
    resultado = numero_1 - numero_2
    print(f"La resta de {numero_1} y {numero_2} es: {resultado}")
elif opcion == '3':
    resultado = numero_1 * numero_2
    print(f"La multiplicación de {numero_1} y {numero_2} es: {resultado}")
else:
    print("Opción no válida. Por favor, elija 1, 2 o 3.")
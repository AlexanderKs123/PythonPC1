
lista_original = [1, 1, 2, 3, 4, 4, 5, 1]

# En esta parte convertimos la lista a un conjunto para eliminar duplicados y luego volver a convertir a lista
lista_procesada = list(set(lista_original))

# En esta parte se muestra el resultado
print("Lista original:", lista_original)
print("Lista procesada:", lista_procesada)
# En esta parte solicitamos el nombre_archivo
nombre_archivo = input("Ingrese el nombre del archivo: ")

# Obtener la extensión del archivo (sufijo) en minúsculas
sufijo = nombre_archivo.lower().split('.')[-1]

# Definir un diccionario de tipos MIME
tipos_mime = {
    'gif': 'image/gif',
    'jpg': 'image/jpeg',
    'jpeg': 'image/jpeg',
    'png': 'image/png',
    'pdf': 'application/pdf',
    'txt': 'text/plain',
    'zip': 'application/zip'
}

# En esta parte obtenemos el tipo MIME correspondiente o 'application/octet-stream' si no se encuentra
tipo_mime = tipos_mime.get(sufijo, 'application/octet-stream')

# Aqui se imprime el resultado
print(f"Tipo MIME para {nombre_archivo}: {tipo_mime}")
# Solicitar al usuario el nombre del archivo
nombre_archivo = input("Ingrese el nombre del archivo: ")

# Obtener el nombre del archivo y la extensión utilizando métodos de cadena
nombre, extension = nombre_archivo.rsplit('.', 1)
nombre = nombre.lower()  # Convertir a minúsculas para manejar sin importar mayúsculas/minúsculas

# Definir un diccionario de tipos MIME
tipos_mime = {
    'gif': 'image/gif',
    'jpg': 'image/jpeg',
    'jpeg': 'image/jpeg',
    'png': 'image/png',
    'pdf': 'application/pdf',
    'txt': 'text/plain',
    'aac': 'audio/aac',
    'avi': 'video/x-msvideo',
    'mp3': 'audio/mpeg',
    'weba': 'audio/webm',
    'webm': 'video/webm'
}

# En esta parte obtenemos el tipo MIME correspondiente o 'application/octet-stream' si no se encuentra
tipo_mime = tipos_mime.get(extension, 'application/octet-stream')

#En esta parte se muestra el resultado
print(f"Nombre del archivo: {nombre}")
print(f"Extensión del archivo: {extension}")
print(f"Tipo MIME para {nombre_archivo}: {tipo_mime}")
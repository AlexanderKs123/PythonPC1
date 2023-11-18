
hora_usuario = input("Ingrese la hora en formato de 24 horas (HH:MM): ")

# En esta parte extraemos la parte de la hora y los minutos
hora, minutos = map(int, hora_usuario.split(':'))

# En esta parte Verificamos si es hora de desayunar, almorzar o cenar
if 7 <= hora < 8:
    print("desayunar.")
elif 12 <= hora < 13:
    print("almorzar.")
elif 18 <= hora < 19:
    print("cenar.")
else:
    # Si no es hora de ninguna comida, no imprimir nada
    pass
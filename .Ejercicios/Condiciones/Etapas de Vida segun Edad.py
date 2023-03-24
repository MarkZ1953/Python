edad = int(input("Proporciona tu edad : "))

if edad > 0 and edad < 10:
    mensaje = "La infancia es increible..."
elif edad >= 10 and edad < 20:
    mensaje = "Muchos cambios y mucho estudio..."
elif edad >= 20 and edad < 30:
    mensaje = "Amor y comienza el trabajo..."
else:
    mensaje = "Etapa de vida no reconocida"

print(f"Tu edad es : {edad} {mensaje}")
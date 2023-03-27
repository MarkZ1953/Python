# Closures
# Las funciones internas pueden capturar y guardar el estado de la funcion externa
def hablar(texto, volumen):
    # La funcion interna ya no recibe parametros
    # Utiliza el estado de la funcion padre (externa)
    def minusculas():
        return texto.lower()

    def mayusculas():
        return texto.upper()

    if volumen > 0.5:
        return mayusculas()
    else:
        return minusculas()


print(hablar('hablo fuerte...', 0.8))
print(hablar('Hablo Suave..', 0.1))


# Otro ejemplo de closure
# Podemos preconfigurar una funcion
def mostrar(titulo):
    # Definimos la funcion anidada
    def saludar(mensaje):
        return titulo + '. ' + mensaje

    return saludar


mostrar_ing = mostrar('Ingeniero')
mostrar_lic = mostrar('Licenciado')

# Podemos seguir usando el estado de la funcion previsamente configurada
# aunque el valor de titulo ya esta fuera del alcance (scope)
print(mostrar_ing('Alvaro Ruiz'))
print(mostrar_lic('Carlos Esparza'))

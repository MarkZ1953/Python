# Funciones Anidadas
def mostrar(texto):
    # Definicion de la funcion interna o anidada
    def convetir_minusculas(t):
        return t.lower()

    # Una vez definida la funcion interna, la mandamos llamar
    return convetir_minusculas(texto)


# Cada vez que se llama la funcion mostrar
# se crea la funcion interna convetir_minusculas
print(mostrar('Desde funcion anidada...'))


# No podemos utilizar la funcion interna desde fuera de la funcion externa
# convetir_minusculas('texto1')
# mostrar.convertir_minusculas('texto1')

# Retornar la funcion anidada
# Observar que en ningun momento se llama la funcion anidada desde la funcion externa
def hablar(volumen):
    def minusculas(texto):
        return texto.lower()

    def mayusculas(texto):
        return texto.upper()

    if volumen > 0.5:
        return mayusculas
    else:
        return minusculas


# Utilizamos la funcion anidada
print(hablar(0.6)('hablo fuerte...'))
print(hablar(0.2)('Hablo Suave...'))

variable_minusculas = hablar(0.4)
print(variable_minusculas('Hablo Suave Nuevamente'))

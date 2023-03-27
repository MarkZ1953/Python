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

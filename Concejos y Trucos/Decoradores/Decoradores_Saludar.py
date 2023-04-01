
# Decorador que convierte el texto a mayusculas
def mayusculas(funcion_a_decorar):
    def envolvente():
        # Mandamos a llamar la funcion original (closure)
        print('antes de la llamada a la funcion a decorar...')
        resultado_original = funcion_a_decorar()
        print(resultado_original)
        print('despues de la llamada a la funcion a decorar...')
        resultado_modificado = resultado_original.upper()
        return resultado_modificado
    return envolvente

@mayusculas
def saludar_minusculas():
    return 'hola..'

# La funcion devuelta por el decorador (envolvente) se ejecuta de manera inmediata
print(saludar_minusculas())
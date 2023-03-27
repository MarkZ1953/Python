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

########################
# La funcion callable nos permite saber si un objeto se puede llamar o no
# Todas las funciones en python son objetos
# Pero no todos en python son funciones
print(f'Se puede llamar el objeto mostrar como funcion?: {callable(mostrar)}')
print(f'Se puede llamar el objeto hablar como funcion?: {callable(hablar)}')
print(f'Se puede llamar el objeto mostrar_ing como funcion?: {callable(mostrar_ing)}')
print(f'Se puede llamar el objeto str como funcion?: {callable("cualquier texto")}')


# Si queremos que una clase defina objetos que se puedan llamar como funciones
# tenemos que sobreescribir el metodo __call__
class Mostrar:
    def __init__(self, titulo):
        self.titulo = titulo

    def __call__(self, mensaje):
        return self.titulo + '. ' + mensaje


mostrar_doctor = Mostrar('Doctor')
print(mostrar_doctor('Carlos Ugalde'))
print(f'Se puede llamar el objeto mostrar_doctor como funcion?: {callable(mostrar_doctor)}')

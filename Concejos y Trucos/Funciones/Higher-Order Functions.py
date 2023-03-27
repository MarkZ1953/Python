# Podemos pasar funciones a otras funciones
# Este tipo de funciones se conocen como higher-order functions
def mayusculas(texto: str):
    return texto.upper()


def minusculas(texto: str):
    return texto.lower()


def saludar(argumento_funcion):
    # Usamos la funcion que recibinmos como argumento y devolvemos la referencia de esta funcion
    referencia_funcion_retornada = argumento_funcion("Hola, saludos desde mi funcion")
    print(referencia_funcion_retornada)


# Llamamos la funcion saludar, pasamos la referencia de una funcion como argumento
saludar(mayusculas)

# Podemos pasar una nueva implemetacion de la funcion que pasamos como argumento
saludar(minusculas)

# El clasico ejemplo de higher-order functions es la funcion map
# Esta funcion toma una funcion como referencia, y un iterable, llama a la funcion
# en cada elemento del iterable proporcionado.
print(list(map(mayusculas, ["texto1", "texto2", "texto3"])))
print(list(map(minusculas, ["texto1", "texto2", "texto3"])))

# Las funciones lamba nos permiten declrar funciones anonimas
# en una sola linea de codigo
# Ejemplo normal
def sumar(a, b):
    return a + b


print(sumar(3, 5))

# Funcion lambda
sumar_lamba = lambda a, b: a + b
print(sumar_lamba(3, 5))

# Utilizando una sola linea de codigo
print((lambda a, b: a + b)(5, 6))

# Podemos usar una funcion lamba siempre que necesitemos una funcion muy concreta
# Por ejemplo ordenar una lista de tuplas, por su segundo valor proporcionando una llave (key)
lista_tuplas = [(1, "b"), (5, "a"), (2, "c"), (3, "d"), (4, "g"), (6, "f")]
# lista_tuplas_ordenada = sorted(lista_tuplas, key=lambda tupla: tupla[0], reverse=True)
lista_tuplas_ordenada = sorted(lista_tuplas, key=lambda tupla: tupla[1])
print(lista_tuplas_ordenada)

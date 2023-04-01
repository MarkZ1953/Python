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

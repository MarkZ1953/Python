# Declaramos el diccionario que contiene numeros de 1 a 11
# Le damos valores usando List Comprehension
numeros = {i: i for i in range(1, 11)}
print(numeros)

# Declaramos la variable suma, la cual contiene la suma de los valores de el diccionario numeros
suma = sum(numeros.values())
print(suma)

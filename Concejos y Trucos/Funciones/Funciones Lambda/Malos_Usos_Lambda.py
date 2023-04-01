
# Ejemplos de casos de funciones lambda que no son recomendables
class Prueba:
    mostrar = lambda self: print('Funcion mostrar...')
    saludar = lambda self: print('Funcion saludar...')

prueba = Prueba()
prueba.mostrar()
prueba.saludar()

# Otro ejemplo donde una funcion lambda agregaria complejidad innecesaria
lista_pares = list(filter(lambda valor: valor % 2 == 0, range(10)))
print(lista_pares)

# Resolviendo el mismo ejercicio pero utilizando list comprehensions
lista_pares_modificada = [valor for valor in range(10) if valor % 2 == 0]
print(lista_pares_modificada)
print("Programa de becas 2022")
print("")

distancia_escuela = int(input("Ingrese la distancia en Km: "))
numero_hermanos = int(input("Ingrese la cantidad de hermanos: "))
salario_familiar = int(input("Ingrese el salario en promedio anual: "))

if distancia_escuela > 40 and numero_hermanos > 2 and salario_familiar <= 20000:
    print("Tienes derecho a la beca completa")
else:
    if numero_hermanos > 2 and salario_familiar <= 20000:
        print("Tienes derecho a la beca pero solo del 80%")
    else:
        if salario_familiar <= 20000:
            print("Tienes derecho a la beca pero solo del 50%")
        else:
            print("No tiene derecho a la beca")
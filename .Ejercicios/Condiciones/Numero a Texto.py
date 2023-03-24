numero = int(input("Ingrese un valor entre 1 y 3 : "))
numerotexto = ""

if numero == 1:
    numerotexto = "Numero Uno"
elif numero == 2:
    numerotexto = "Numero Dos"
elif numero == 3:
    numerotexto = "Numero Tres"
else:
    print("Valor no reconocido")

print(f"Numero proporcionado {numero} - {numerotexto}")
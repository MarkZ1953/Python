emailusu = False

emailusu = input("Introduce tu Correo electronico : ")

for i in emailusu:
    if (i=="@"):
        email = True

if email == True:
    print("El email "+ emailusu +" es correcto")
else:
    print("El email "+ emailusu +" es incorrecto")


contador = 0

emailusu = input("Introduce tu Correo electronico : ")

for i in emailusu:
    if i=="@" or i==".":
        contador = contador+1

if contador >= 2:
    print("El email "+ emailusu +" es correcto")
else:
    print("El email "+ emailusu +" es incorrecto")

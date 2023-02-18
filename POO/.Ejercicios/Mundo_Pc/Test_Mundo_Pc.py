from Teclado import Teclado
from Raton import Raton
from Monitor import Monitor
from Computadora import Computadora
from Orden import Orden

monitor1 = Monitor("HP",27)
raton1 = Raton("HP","USB")
teclado1 = Teclado("HP","USB")

monitor2 = Monitor("Acer",27)
teclado2 = Teclado("Acer","Bluetooth")
raton2 = Raton("Acer","Bluetooth")

computadora1 = Computadora("HP",monitor1,teclado1,raton1)
computadora2 = Computadora("Acer",monitor2,teclado2,raton2)

computadoras = [computadora1,computadora2]
orden1 = Orden(computadoras=computadoras)

monitor3 = Monitor("Microsoft",27)
raton3 = Raton("Microsoft","USB")
teclado3 = Teclado("Microsoft","USB")

monitor4 = Monitor("Acer",27)
teclado4 = Teclado("Acer","Bluetooth")
raton4 = Raton("Acer","Bluetooth")

computadora3 = Computadora("Microsoft",monitor3,teclado3,raton3)
computadora4 = Computadora("Microsoft",monitor4,teclado4,raton4)

computadoras2 = [computadora3,computadora4]

orden2 = Orden(computadoras2)

print(orden1)
print(orden2)
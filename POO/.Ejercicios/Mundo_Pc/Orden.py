from Computadora import Computadora

class Orden:
    contadorOrdenes = 0

    @classmethod
    def generar_siguiente_valor(cls):
        cls.contadorOrdenes += 1
        return cls.contadorOrdenes

    def __init__(self,computadoras) -> None:
        self._Id_Orden = self.generar_siguiente_valor()
        self._computadoras = computadoras

    def agregar_computadora(self,computadora):
        self._computadoras.append(computadora)

    def __str__(self) -> str:
        computadoras_str = ""
        for computadora in self._computadoras:
            computadoras_str += computadora.__str__()
        return f"Orden : {self._Id_Orden}\nComputadoras : {computadoras_str}"
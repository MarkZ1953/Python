class Computadora:
    contadorComputadoras = 0

    @classmethod
    def generar_siguiente_valor(cls):
        cls.contadorComputadoras += 1
        return cls.contadorComputadoras

    def __init__(self,nombre,monitor,teclado,raton) -> None:
        self.Id_Computadora = self.generar_siguiente_valor()
        self._teclado = teclado
        self._raton = raton
        self._nombre = nombre
        self._monitor = monitor

    def __str__(self) -> str:
        return f"\n\t{f'Computadora {self._nombre}:{self.Id_Computadora}'.center(40,'-')}\n{self._monitor}\n{self._teclado}\n{self._raton}\n\t{''.center(40,'-')}"
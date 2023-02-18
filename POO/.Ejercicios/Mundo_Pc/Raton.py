from DispositivoEntrada import DispositivoEntrada

class Raton(DispositivoEntrada):
    contadorRatones = 0

    @classmethod
    def generar_siguiente_valor(cls):
        cls.contadorRatones += 1
        return cls.contadorRatones

    def __init__(self, marca: str, tipoEntrada: str) -> None:
        super().__init__(marca, tipoEntrada)
        self.Id_Raton = self.generar_siguiente_valor()
        
    def __str__(self) -> str:
        return f"\tRaton :\n\t\tId : {self.Id_Raton}\n\t\tMarca : {self._marca}\n\t\tTipo de Entrada : {self._tipoEntrada}"
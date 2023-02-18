from DispositivoEntrada import DispositivoEntrada

class Teclado(DispositivoEntrada):
    contadorTeclados = 0

    @classmethod
    def generar_siguiente_valor(cls):
        cls.contadorTeclados += 1
        return cls.contadorTeclados

    def __init__(self, marca:str, tipoEntrada:str) -> None:
        super().__init__(marca, tipoEntrada)
        self.Id_Teclado = self.generar_siguiente_valor()

    def __str__(self) -> str:
        return f"\tTeclado :\n\t\tId : {self.Id_Teclado}\n\t\tMarca : {self._marca}\n\t\tTipo de Entrada : {self._tipoEntrada}"


if __name__ == "__main__":
    teclado1 = Teclado("HP","USB")
    print("Propiedades Teclado".center(30,"-"))
    print(teclado1)
    print("".center(30,"-"))
class Monitor:
    contadorMonitores = 0

    @classmethod
    def generar_siguiente_valor(cls):
        cls.contadorMonitores += 1
        return cls.contadorMonitores

    def __init__(self,marca:str,tamaño:int) -> None:
        self.Id_Monitor = self.generar_siguiente_valor()
        self._tamaño = tamaño
        self._marca = marca
    
    def __str__(self) -> str:
        return f"\tMonitor :\n\t\tId : {self.Id_Monitor}\n\t\tMarca : {self._marca}\n\t\tTamaño : {self._tamaño}"

if __name__ == "__main__":  
    monitor1 = Monitor("HP",27)
    print("Propiedades Monitor".center(30,"-"))
    print(monitor1)
    print("".center(30,"-"))
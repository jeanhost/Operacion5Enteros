class OperacionesEnteros:
    def __init__(self, numeros):
        self.__numeros = numeros

    def MCD(self, numero1, numero2):
        temporal = 0
        while numero2 != 0:
            temporal = numero2
            numero2 = numero1 % numero2
            numero1 = temporal
        return numero1

    def calcularMCD(self):
        return None
from abc import ABC, abstractmethod


class EstrategiaDescuento(ABC):

    @abstractmethod
    def calcular_precio(self, monto):
        pass
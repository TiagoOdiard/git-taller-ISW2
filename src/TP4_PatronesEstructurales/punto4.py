from abc import ABC, abstractmethod

# ==========================
# Componente base
# ==========================
class Componente(ABC):
    @abstractmethod
    def valor(self):
        pass


# ==========================
# Clase concreta (número)
# ==========================
class Numero(Componente):
    def __init__(self, valor):
        self._valor = valor

    def valor(self):
        return self._valor


# ==========================
# Decorador base
# ==========================
class OperacionDecorator(Componente):
    def __init__(self, componente: Componente):
        self._componente = componente

    @abstractmethod
    def valor(self):
        pass


# ==========================
# Decoradores concretos
# ==========================
class Sumar2(OperacionDecorator):
    def valor(self):
        return self._componente.valor() + 2


class Multiplicar2(OperacionDecorator):
    def valor(self):
        return self._componente.valor() * 2


class Dividir3(OperacionDecorator):
    def valor(self):
        return self._componente.valor() / 3


# ==========================
# Uso
# ==========================
if __name__ == "__main__":

    numero = Numero(10)

    print("Valor original:")
    print(numero.valor())

    print("\nSumar 2:")
    op1 = Sumar2(numero)
    print(op1.valor())

    print("\nSumar 2 y luego multiplicar por 2:")
    op2 = Multiplicar2(Sumar2(numero))
    print(op2.valor())

    print("\nSumar 2, multiplicar por 2 y dividir por 3:")
    op3 = Dividir3(Multiplicar2(Sumar2(numero)))
    print(op3.valor())
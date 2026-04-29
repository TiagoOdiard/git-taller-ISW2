from __future__ import annotations
from abc import ABC, abstractmethod

#*------------------------------------------------------------------------
#* Interfaces de los Productos (Abstract Products)
#*------------------------------------------------------------------------
class Hamburguesa(ABC):
    @abstractmethod
    def obtener_descripcion(self) -> str:
        pass

class Bebida(ABC):
    @abstractmethod
    def servir(self) -> str:
        pass

#*------------------------------------------------------------------------
#* Fábrica Abstracta (Abstract Factory)
#*------------------------------------------------------------------------
class FastFoodFactory(ABC):
    @abstractmethod
    def crear_hamburguesa(self) -> Hamburguesa:
        pass

    @abstractmethod
    def crear_bebida(self) -> Bebida:
        pass

#*------------------------------------------------------------------------
#* Familia 1: Combo Tradicional (Concrete Products & Factory)
#*------------------------------------------------------------------------
class HamburguesaClasica(Hamburguesa):
    def obtener_descripcion(self) -> str:
        return "Hamburguesa con queso y lechuga"

class GaseosaCola(Bebida):
    def servir(self) -> str:
        return "Gaseosa cola con hielo"

class FactoryTradicional(FastFoodFactory):
    def crear_hamburguesa(self) -> Hamburguesa:
        return HamburguesaClasica()
    def crear_bebida(self) -> Bebida:
        return GaseosaCola()

#*------------------------------------------------------------------------
#* Familia 2: Combo Vegano (Concrete Products & Factory)
#*------------------------------------------------------------------------
class HamburguesaLentejas(Hamburguesa):
    def obtener_descripcion(self) -> str:
        return "Hamburguesa de lentejas y palta"

class JugoNatural(Bebida):
    def servir(self) -> str:
        return "Jugo de naranja exprimido"

class FactoryVegana(FastFoodFactory):
    def crear_hamburguesa(self) -> Hamburguesa:
        return HamburguesaLentejas()
    def crear_bebida(self) -> Bebida:
        return JugoNatural()

#*------------------------------------------------------------------------
#* Código Cliente
#*------------------------------------------------------------------------
def preparar_combo(factory: FastFoodFactory) -> None:
    """
    El cliente trabaja con fábricas y productos a través de interfaces 
    abstractas, garantizando que el combo sea consistente.
    """
    hamburguesa = factory.crear_hamburguesa()
    bebida = factory.crear_bebida()

    print(f"Preparando: {hamburguesa.obtener_descripcion()}")
    print(f"Acompañamiento: {bebida.servir()}")

if __name__ == "__main__":
    print("Cliente: Pedido de un Combo Tradicional:")
    preparar_combo(FactoryTradicional())

    print("\nCliente: Pedido de un Combo Vegano:")
    preparar_combo(FactoryVegana())
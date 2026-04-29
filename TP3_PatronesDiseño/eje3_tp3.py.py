from __future__ import annotations
from abc import ABC, abstractmethod

#*------------------------------------------------------------------------
#* Producto Base (Interface)
#*------------------------------------------------------------------------
class Hamburguesa(ABC):
    @abstractmethod
    def entregar(self) -> str:
        pass

#*------------------------------------------------------------------------
#* Productos Concretos
#*------------------------------------------------------------------------
class HamburguesaMostrador(Hamburguesa):
    def entregar(self) -> str:
        return "entregada en mostrador"

class HamburguesaRetiro(Hamburguesa):
    def entregar(self) -> str:
        return "retirada por el cliente"

class HamburguesaDelivery(Hamburguesa):
    def entregar(self) -> str:
        return "enviada por delivery"

#*------------------------------------------------------------------------
#* Creador (Abstract Factory Method)
#*------------------------------------------------------------------------
class Despacho(ABC):
    @abstractmethod
    def factory_method(self):
        pass

    def gestionar_entrega(self) -> str:
        # Llama al factory method para crear el objeto de producto
        hamburguesa = self.factory_method()
        # Usa el producto
        return f"Pedido: La hamburguesa ha sido {hamburguesa.entregar()}."

#*------------------------------------------------------------------------
#* Creadores Concretos
#*------------------------------------------------------------------------
class DespachoMostrador(Despacho):
    def factory_method(self) -> Hamburguesa:
        return HamburguesaMostrador()

class DespachoRetiro(Despacho):
    def factory_method(self) -> Hamburguesa:
        return HamburguesaRetiro()

class DespachoDelivery(Despacho):
    def factory_method(self) -> Hamburguesa:
        return HamburguesaDelivery()

#*------------------------------------------------------------------------
#* Código Cliente
#*------------------------------------------------------------------------
def realizar_pedido(despachador: Despacho) -> None:
    print(f"{despachador.gestionar_entrega()}")

if __name__ == "__main__":
    print("--- Sistema de Gestión de Hamburguesas ---")
    
    print("\nCaso 1:")
    realizar_pedido(DespachoMostrador())

    print("\nCaso 2:")
    realizar_pedido(DespachoRetiro())

    print("\nCaso 3:")
    realizar_pedido(DespachoDelivery())
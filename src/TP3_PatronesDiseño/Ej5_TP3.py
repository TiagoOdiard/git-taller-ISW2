from __future__ import annotations
from abc import ABC, abstractmethod

class Avion:
    """Producto complejo que se construye paso a paso."""

    def __init__(self) -> None:
        self.partes = []

    def agregar(self, parte: str) -> None:
        self.partes.append(parte)

    def mostrar(self) -> str:
        return "Avión con:\n  - " + "\n  - ".join(self.partes)


class BuilderAvion(ABC):
    """Interfaz abstracta del Builder."""

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._producto = Avion()

    def obtener_resultado(self) -> Avion:
        producto = self._producto
        self.reset()
        return producto

    @abstractmethod
    def construir_body(self) -> None:
        pass

    @abstractmethod
    def construir_turbinas(self) -> None:
        pass

    @abstractmethod
    def construir_alas(self) -> None:
        pass

    @abstractmethod
    def construir_tren_aterrizaje(self) -> None:
        pass


class BuilderAvionComercial(BuilderAvion):
    """Builder concreto para un avión comercial."""

    def construir_body(self) -> None:
        self._producto.agregar("Body de avión comercial")

    def construir_turbinas(self) -> None:
        self._producto.agregar("2 turbinas grandes")

    def construir_alas(self) -> None:
        self._producto.agregar("2 alas amplias")

    def construir_tren_aterrizaje(self) -> None:
        self._producto.agregar("Tren de aterrizaje reforzado")


class BuilderAvionPrivado(BuilderAvion):
    """Builder concreto para un avión privado."""

    def construir_body(self) -> None:
        self._producto.agregar("Body de avión privado")

    def construir_turbinas(self) -> None:
        self._producto.agregar("2 turbinas pequeñas")

    def construir_alas(self) -> None:
        self._producto.agregar("2 alas compactas")

    def construir_tren_aterrizaje(self) -> None:
        self._producto.agregar("Tren de aterrizaje liviano")


class Director:
    """Define el orden de construcción."""

    def __init__(self, builder: BuilderAvion) -> None:
        self._builder = builder

    def construir_avion_basico(self) -> None:
        self._builder.construir_body()
        self._builder.construir_alas()

    def construir_avion_completo(self) -> None:
        self._builder.construir_body()
        self._builder.construir_alas()
        self._builder.construir_turbinas()
        self._builder.construir_tren_aterrizaje()


def main() -> None:
    # Avión comercial
    builder_comercial = BuilderAvionComercial()
    director = Director(builder_comercial)

    director.construir_avion_completo()
    avion1 = builder_comercial.obtener_resultado()
    print("Avión Comercial:")
    print(avion1.mostrar())
    print()

    # Avión privado
    builder_privado = BuilderAvionPrivado()
    director = Director(builder_privado)

    director.construir_avion_completo()
    avion2 = builder_privado.obtener_resultado()
    print("Avión Privado:")
    print(avion2.mostrar())


if __name__ == "__main__":
    main()
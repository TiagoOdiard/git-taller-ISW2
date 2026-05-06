from abc import ABC, abstractmethod

# ==========================
# Implementador (Bridge)
# ==========================
class TrenLaminador(ABC):
    @abstractmethod
    def producir(self, espesor, ancho):
        pass


# Implementaciones concretas
class Tren5m(TrenLaminador):
    def producir(self, espesor, ancho):
        print(f"Produciendo lámina de {espesor}\" x {ancho}m x 5m de largo")


class Tren10m(TrenLaminador):
    def producir(self, espesor, ancho):
        print(f"Produciendo lámina de {espesor}\" x {ancho}m x 10m de largo")


# ==========================
# Abstracción
# ==========================
class Lamina:
    def __init__(self, espesor, ancho, tren: TrenLaminador):
        self.espesor = espesor
        self.ancho = ancho
        self.tren = tren  # Bridge hacia la implementación

    def set_tren(self, tren: TrenLaminador):
        self.tren = tren

    def producir(self):
        self.tren.producir(self.espesor, self.ancho)


# ==========================
# Uso
# ==========================
if __name__ == "__main__":
    tren5 = Tren5m()
    tren10 = Tren10m()

    # Lámina genérica
    lamina = Lamina(0.5, 1.5, tren5)

    print("\n--- Producción con tren de 5m ---")
    lamina.producir()

    print("\n--- Cambio a tren de 10m ---")
    lamina.set_tren(tren10)
    lamina.producir()
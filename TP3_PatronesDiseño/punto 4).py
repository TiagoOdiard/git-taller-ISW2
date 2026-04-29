from abc import ABC, abstractmethod

# =========================
# Clase base
# =========================

class Impuesto(ABC):
    @abstractmethod
    def calcular(self, base: float) -> float:
        pass


# =========================
# Clases concretas
# =========================

class IVA(Impuesto):
    def calcular(self, base: float) -> float:
        return base * 0.21


class IIBB(Impuesto):
    def calcular(self, base: float) -> float:
        return base * 0.05


class Contribuciones(Impuesto):
    def calcular(self, base: float) -> float:
        return base * 0.012


# =========================
# Factory
# =========================

class ImpuestoFactory:
    @staticmethod
    def crear_impuesto(tipo: str) -> Impuesto:
        tipo = tipo.lower()

        if tipo == "iva":
            return IVA()
        elif tipo == "iibb":
            return IIBB()
        elif tipo == "contribuciones":
            return Contribuciones()
        else:
            raise ValueError("Tipo de impuesto no válido")


# =========================
# Cliente
# =========================

class Calculadora:
    def __init__(self):
        self.factory = ImpuestoFactory()

    def calcular_total(self, base: float):
        tipos = ["iva", "iibb", "contribuciones"]

        total_impuestos = 0

        for tipo in tipos:
            impuesto = self.factory.crear_impuesto(tipo)
            total_impuestos += impuesto.calcular(base)

        return base + total_impuestos


# =========================
# Main
# =========================

def main():
    calc = Calculadora()

    base = 100000
    total = calc.calcular_total(base)

    print("Total con impuestos:", total)


if __name__ == "__main__":
    main()


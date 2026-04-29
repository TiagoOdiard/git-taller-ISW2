import copy
from abc import ABC, abstractmethod

# =========================
# Prototype
# =========================

class Prototype(ABC):
    @abstractmethod
    def clone(self):
        pass


# =========================
# Clase concreta
# =========================

class CalculadoraImpuestos(Prototype):

    def __init__(self, iva, iibb, contribuciones):
        self.iva = iva
        self.iibb = iibb
        self.contribuciones = contribuciones

    def calcular_total(self, base):
        return base + (base * self.iva) + (base * self.iibb) + (base * self.contribuciones)

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return f"IVA: {self.iva}, IIBB: {self.iibb}, Contribuciones: {self.contribuciones}"


# =========================
# Main
# =========================

def main():
    # Prototipo base
    calculadora_base = CalculadoraImpuestos(0.21, 0.05, 0.012)

    print("Calculadora original:")
    print(calculadora_base)

    # Clonamos
    calculadora_modificada = calculadora_base.clone()

    # Modificamos el clon (por ejemplo otro régimen)
    calculadora_modificada.iva = 0.105  # IVA reducido

    print("\nCalculadora clonada y modificada:")
    print(calculadora_modificada)

    print("\nCalculadora original (no cambia):")
    print(calculadora_base)

    # Uso real
    base = 100000
    print("\nTotal original:", calculadora_base.calcular_total(base))
    print("Total modificado:", calculadora_modificada.calcular_total(base))


if __name__ == "__main__":
    main()

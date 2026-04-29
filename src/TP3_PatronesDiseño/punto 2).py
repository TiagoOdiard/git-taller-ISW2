class CalculadoraImpuestos:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
        return cls._instancia

    def __init__(self):
        # Evita reinicialización
        if not hasattr(self, "_inicializado"):
            self._inicializado = True

    def calcular_total_con_impuestos(self, base_imponible: float) -> float:
        iva = base_imponible * 0.21      # 21%
        iibb = base_imponible * 0.05     # 5%
        contribuciones = base_imponible * 0.012  # 1.2%

        total = base_imponible + iva + iibb + contribuciones
        return total


# =========================
# Simulación de uso en distintas clases
# =========================

class Factura:
    def __init__(self, base):
        self.base = base
        self.calculadora = CalculadoraImpuestos()

    def calcular_total(self):
        return self.calculadora.calcular_total_con_impuestos(self.base)


class Pedido:
    def __init__(self, base):
        self.base = base
        self.calculadora = CalculadoraImpuestos()

    def calcular_total(self):
        return self.calculadora.calcular_total_con_impuestos(self.base)


# =========================
# Programa principal
# =========================

def main():
    factura = Factura(100000)
    pedido = Pedido(50000)

    print("Total factura:", factura.calcular_total())
    print("Total pedido:", pedido.calcular_total())

    # Verificación de Singleton
    calc1 = CalculadoraImpuestos()
    calc2 = CalculadoraImpuestos()
    print("¿Es la misma instancia?", calc1 is calc2)


if __name__ == "__main__":
    main()
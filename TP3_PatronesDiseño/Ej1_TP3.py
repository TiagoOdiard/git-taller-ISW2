from threading import Lock


class FactorialCalculator:
    """
    Singleton para calcular factoriales.
    """

    _instancia = None
    _lock = Lock()

    def __new__(cls, *args, **kwargs):
        if cls._instancia is None:
            with cls._lock:
                if cls._instancia is None:
                    cls._instancia = super().__new__(cls)
        return cls._instancia

    def __init__(self):
        if not hasattr(self, "_inicializado"):
            self._inicializado = True

    def calcular_factorial(self, n: int) -> int:
        if n < 0:
            raise ValueError("El factorial no esta definido para números negativos")

        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        return resultado


def main():
    # Primera instancia
    calc1 = FactorialCalculator()

    # Segunda "instancia"
    calc2 = FactorialCalculator()

    print("¿Son la misma instancia?", calc1 is calc2)

    # Uso del factorial
    print("Factorial de 5:", calc1.calcular_factorial(5))
    print("Factorial de 6 (desde calc2):", calc2.calcular_factorial(6))


if __name__ == "__main__":
    main()
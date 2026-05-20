from abc import ABC, abstractmethod


class Numero:
    """Representa la solicitud que viaja por la cadena"""

    def __init__(self, valor: int) -> None:
        self.valor = valor


class ManejadorNumeros(ABC):
    """Handler abstracto que maneja la estructura de la cadena"""

    def __init__(self) -> None:
        self._siguiente: "ManejadorNumeros" | None = None

    def establecer_siguiente(
        self, manejador: "ManejadorNumeros"
    ) -> "ManejadorNumeros":
        self._siguiente = manejador
        return manejador  # Permite encadenamiento

    @abstractmethod
    def procesar(self, numero: Numero) -> None:
        pass


class ManejadorPrimos(ManejadorNumeros):
    """Consume el número si este es primo."""

    def _es_primo(self, n: int) -> bool:
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def procesar(self, numero: Numero) -> None:
        if self._es_primo(numero.valor):
            print(f"[Manejador Primos] -> Consumió el número {numero.valor}")
        elif self._siguiente:
            self._siguiente.procesar(numero)
        else:
            print(
                f"[Fin de Cadena] -> El número {numero.valor} NO fue consumido por nadie."
            )


class ManejadorPares(ManejadorNumeros):
    """Consume el número si este es par."""

    def procesar(self, numero: Numero) -> None:
        if numero.valor % 2 == 0:
            print(f"[Manejador Pares]  -> Consumió el número {numero.valor}")
        elif self._siguiente:
            self._siguiente.procesar(numero)
        else:
            print(
                f"[Fin de Cadena] -> El número {numero.valor} NO fue consumido por nadie."
            )


def main() -> None:
    # Intancias de los manejadores de la cadena
    manejador_primos = ManejadorPrimos()
    manejador_pares = ManejadorPares()

  
    manejador_primos.establecer_siguiente(manejador_pares)

    #  Generar y pasar los números del 1 al 100
    print("--- Iniciando procesamiento de la cadena (1 al 100) ---\n")
    for i in range(1, 101):
        num_solicitud = Numero(i)
        manejador_primos.procesar(num_solicitud)


if __name__ == "__main__":
    main()
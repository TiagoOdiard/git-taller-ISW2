from typing import Iterator


class CadenaIterables:
    """Colección que almacena una cadena de caracteres
    
    Proporciona mecanismos para recorrer sus caracteres de forma uniforme
    en sentido directo y reverso.
    """

    def __init__(self, texto: str) -> None:
        self._texto = texto

    def sentido_directo(self) -> Iterator[str]:
        """Iterator concreto, recorre la cadena completa.
      
        """
        for caracter in self._texto:
            yield caracter

    def sentido_reverso(self) -> Iterator[str]:
        """Iterator concreto, recorre la cadena desde el último carácter hasta el primero.
        """
        # Recorremos la cadena desde el índice final hasta el 0
        for i in range(len(self._texto) - 1, -1, -1):
            yield self._texto[i]


def main() -> None:
    # Creamos la colección con la palabra "UADER"
    mi_cadena = CadenaIterables("UADER")

    print(f"Texto original: {mi_cadena._texto}\n")

    # Recorrido directo
    print("Recorrido en sentido directo:")
    for caracter in mi_cadena.sentido_directo():
        print(f"- {caracter}")

    print("-" * 30)

    # Recorrido en reversa
    print("Recorrido en sentido reverso:")
    for caracter in mi_cadena.sentido_reverso():
        print(f"- {caracter}")


if __name__ == "__main__":
    main()
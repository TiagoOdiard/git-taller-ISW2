from abc import ABC, abstractmethod

# ==========================
# Componente base
# ==========================
class Componente(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def mostrar(self, nivel=0):
        pass


# ==========================
# Hoja (Leaf)
# ==========================
class Pieza(Componente):
    def mostrar(self, nivel=0):
        print("  " * nivel + f"- Pieza: {self.nombre}")


# ==========================
# Compuesto (Composite)
# ==========================
class Conjunto(Componente):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.hijos = []

    def agregar(self, componente):
        self.hijos.append(componente)

    def mostrar(self, nivel=0):
        print("  " * nivel + f"+ Conjunto: {self.nombre}")
        for hijo in self.hijos:
            hijo.mostrar(nivel + 1)


# ==========================
# Construcción de la estructura
# ==========================
if __name__ == "__main__":

    # Producto principal
    producto = Conjunto("Producto Principal")

    # Crear 3 subconjuntos con 4 piezas cada uno
    for i in range(1, 4):
        subconjunto = Conjunto(f"Subconjunto {i}")
        for j in range(1, 5):
            pieza = Pieza(f"P{i}.{j}")
            subconjunto.agregar(pieza)
        producto.agregar(subconjunto)

    print("\n--- Estructura inicial ---")
    producto.mostrar()

    # ==========================
    # Agregar subconjunto opcional
    # ==========================
    subconjunto_opcional = Conjunto("Subconjunto Opcional")

    for j in range(1, 5):
        pieza = Pieza(f"OP.{j}")
        subconjunto_opcional.agregar(pieza)

    producto.agregar(subconjunto_opcional)

    print("\n--- Con subconjunto opcional ---")
    producto.mostrar()
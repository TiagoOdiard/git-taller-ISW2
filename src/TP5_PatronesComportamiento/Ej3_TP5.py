# Clase Subject (Observable)
class EmisorIDs:
    def __init__(self):
        self.observadores = []

    def suscribir(self, observador):
        self.observadores.append(observador)

    def emitir_id(self, id_emitido):
        print(f"\n[EMISOR] ID emitido: {id_emitido}")

        for observador in self.observadores:
            observador.actualizar(id_emitido)


# Clase Observer
class Observador:
    def __init__(self, nombre, id_propio):
        self.nombre = nombre
        self.id_propio = id_propio

    def actualizar(self, id_emitido):
        if id_emitido == self.id_propio:
            print(f"{self.nombre}: ¡Mi ID ({self.id_propio}) fue detectado!")


# ===== MAIN =====

# Crear el emisor
emisor = EmisorIDs()

# Crear 4 observadores con IDs específicos
obs1 = Observador("ClaseA", "A123")
obs2 = Observador("ClaseB", "B456")
obs3 = Observador("ClaseC", "C789")
obs4 = Observador("ClaseD", "D321")

# Suscribir observadores
emisor.suscribir(obs1)
emisor.suscribir(obs2)
emisor.suscribir(obs3)
emisor.suscribir(obs4)

# Emitir 8 IDs
ids = [
    "A123",  # coincide
    "XXXX",
    "B456",  # coincide
    "ZZZZ",
    "C789",  # coincide
    "1111",
    "D321",  # coincide
    "ABCD"
]

for id_actual in ids:
    emisor.emitir_id(id_actual)
import os

#*--------------------------------------------------------------------
#* Design pattern memento, ejemplo
#*-------------------------------------------------------------------
class Memento:
	def __init__(self, file, content):
		self.file = file
		self.content = content


class FileWriterUtility:
	def __init__(self, file):
		self.file = file
		self.content = ""

	def write(self, string):
		self.content += string

	def save(self):
		return Memento(self.file, self.content)

	def undo(self, memento):
		self.file = memento.file
		self.content = memento.content


class FileWriterCaretaker:
	def __init__(self):
		# Historial para almacenar hasta 4 estados
		self.mementos = []

	def save(self, writer):
		self.mementos.append(writer.save())
		# Si se excede el límite de 4 estados, eliminamos el más antiguo (índice 0)
		if len(self.mementos) > 4:
			self.mementos.pop(0)

	def undo(self, writer, index=0):
		"""
		Recupera un estado pasado.
		index=0 : Inmediato anterior
		index=1, 2, 3 : Estados más antiguos
		"""
		if not self.mementos:
			print("No hay estados guardados para recuperar.")
			return
		
		if index < 0 or index >= len(self.mementos):
			print(f"Error: Índice {index} fuera de rango. Hay {len(self.mementos)} estados guardados.")
			return
		
		# Calculamos el índice negativo para acceder de atrás hacia adelante:
		# index 0 -> -1 (último), index 1 -> -2 (penúltimo), etc.
		target_index = -(index + 1)
		
		memento = self.mementos[target_index]
		writer.undo(memento)


if __name__ == '__main__':

	# Se limpia la consola (compatible con Windows y sistemas basados en Unix)
	os.system("clear" if os.name == "posix" else "cls")
	
	print("Crea un objeto que gestionará las versiones anteriores")
	caretaker = FileWriterCaretaker()

	print("Crea el objeto cuyo estado se quiere preservar")
	writer = FileWriterUtility("GFG.txt")

	# --- Guardando 4 estados ---
	print("\n[Guardando Estado 3] - (El más antiguo de los 4)")
	writer.write("Línea 1: Clase de IS2 en UADER\n")
	caretaker.save(writer)

	print("[Guardando Estado 2]")
	writer.write("Línea 2: Material adicional de la clase de patrones\n")
	caretaker.save(writer)

	print("[Guardando Estado 1]")
	writer.write("Línea 3: Material adicional de la clase de patrones II\n")
	caretaker.save(writer)

	print("[Guardando Estado 0] - (Inmediato anterior)")
	writer.write("Línea 4: Implementación de un historial de Mementos\n")
	caretaker.save(writer)

	# --- Escribiendo sin guardar ---
	print("\nSe graba información adicional pero NO se salva...")
	writer.write("Línea 5: Texto no guardado que se perderá al hacer undo.\n")
	
	print("\n--- Estado actual (antes de undo) ---")
	print(writer.content)

	# --- Pruebas de recuperación en cualquier orden ---
	print("--- Se invoca al <undo> con argumento 0 (inmediato anterior) ---")
	caretaker.undo(writer, 0)
	print(writer.content)

	print("--- Se invoca al <undo> con argumento 2 (tercer estado hacia atrás) ---")
	caretaker.undo(writer, 2)
	print(writer.content)

	print("--- Se invoca al <undo> con argumento 3 (cuarto estado hacia atrás, el más antiguo) ---")
	caretaker.undo(writer, 3)
	print(writer.content)

	print("--- Se invoca al <undo> con argumento 1 (segundo estado hacia atrás) ---")
	caretaker.undo(writer, 1)
	print(writer.content)
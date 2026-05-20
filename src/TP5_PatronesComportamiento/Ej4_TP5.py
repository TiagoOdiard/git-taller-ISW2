import os

#*--------------------------------------------------------------------
#* Ejemplo de design pattern de tipo state
#*--------------------------------------------------------------------
"""State class: Base State class"""
class State:

	def scan(self):
		# Nota: el código original avanza la posición antes de leer, 
		# por lo que el primer elemento que muestra es el índice 1.
		self.pos += 1
		if self.pos == len(self.stations):
			self.pos = 0
		print("Sintonizando... Estación {} {}".format(self.stations[self.pos], self.name))


#*------- Implementa como barrer las estaciones de AM
class AmState(State):

	def __init__(self, radio):
		self.radio = radio
		self.stations = ["1250", "1380", "1510"]
		self.pos = 0
		self.name = "AM"

	def toggle_mode(self):
		print("\n--> Cambiando a Memorias")
		self.radio.state = self.radio.memstate


#*------- Implementa como barrer las estaciones de FM
"""Separate class for FM state"""
class FmState(State):

	def __init__(self, radio):
		self.radio = radio
		self.stations = ["81.3", "89.1", "103.9"]
		self.pos = 0
		self.name = "FM"

	def toggle_mode(self):
		print("\n--> Cambiando a AM")
		self.radio.state = self.radio.amstate


#*------- Implementa como barrer las estaciones Memorizadas (NUEVO ESTADO)
class MemoryState(State):

	def __init__(self, radio):
		self.radio = radio
		# Se agregan las memorias M1 a M4 mezclando frecuencias AM y FM
		self.stations = ["M1 (89.1 FM)", "M2 (1250 AM)", "M3 (103.9 FM)", "M4 (1380 AM)"]
		self.pos = 0
		self.name = "(Modo Memoria)"

	def toggle_mode(self):
		print("\n--> Cambiando a FM")
		self.radio.state = self.radio.fmstate


#*--------- Construye la radio con todas sus formas de sintonía
class Radio:

	def __init__(self):
		self.fmstate = FmState(self)
		self.amstate = AmState(self)
		self.memstate = MemoryState(self) # Inicializamos el nuevo estado

#*--- Inicialmente en FM
		self.state = self.fmstate

	def toggle_mode(self):
		self.state.toggle_mode()

	def scan(self):
		self.state.scan()

#*---------------------

if __name__ == "__main__":
	# Detecta el OS para limpiar la consola correctamente (útil si usas Git Bash o Linux)
	os.system("clear" if os.name == "posix" else "cls")
	
	print("\nCrea un objeto radio y almacena las siguientes acciones")
	radio = Radio()
	
	# Actualizamos las acciones para recorrer los 3 estados. 
	# Hacemos 4 'scans' por estado para asegurar que el modo Memoria barra las 4 frecuencias completas.
	actions = [radio.scan] * 4 + [radio.toggle_mode] + \
	          [radio.scan] * 4 + [radio.toggle_mode] + \
	          [radio.scan] * 4 + [radio.toggle_mode]

#*---- Recorre las acciones ejecutando la acción
	print("Recorre las acciones ejecutando la acción, el objeto cambia la interfaz según el estado\n")
	for action in actions:
		action()
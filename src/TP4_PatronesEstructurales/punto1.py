import os
import platform

class Ping:
    def __init__(self):
        # Detectar sistema operativo para el comando ping
        self.param = "-n" if platform.system().lower() == "windows" else "-c"

    def execute(self, ip: str):
        # Solo permite IPs que empiecen con "192."
        if not ip.startswith("192."):
            print("Error: IP no permitida (debe comenzar con '192.')")
            return

        print(f"Haciendo ping restringido a {ip}...")
        self._ping(ip)

    def executefree(self, ip: str):
        # Sin restricción
        print(f"Haciendo ping libre a {ip}...")
        self._ping(ip)

    def _ping(self, ip: str):
        for i in range(10):
            print(f"Intento {i+1}")
            os.system(f"ping {self.param} 1 {ip}")


# Proxy
class PingProxy:
    def __init__(self):
        self.ping = Ping()

    def execute(self, ip: str):
        # Caso especial
        if ip == "192.168.0.254":
            print("IP especial detectada. Redirigiendo a www.google.com...")
            self.ping.executefree("www.google.com")
        else:
            # Caso normal → pasa por el control
            self.ping.execute(ip)


# ==========================
# Ejemplo de uso
# ==========================
if __name__ == "__main__":
    proxy = PingProxy()

    print("\n--- Caso 1: IP válida ---")
    proxy.execute("192.168.1.1")

    print("\n--- Caso 2: IP inválida ---")
    proxy.execute("10.0.0.1")

    print("\n--- Caso 3: IP especial ---")
    proxy.execute("192.168.0.254")
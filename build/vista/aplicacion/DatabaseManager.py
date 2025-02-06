import pyodbc
from nodos import NODOS

class DatabaseManager:
    def __init__(self):
        self.indice_nodo = 0  # Inicia en Nodo 1
        self.conexion = None
        self.conectar()

    def conectar(self):
        """Conecta al nodo actual."""
        config = NODOS[self.indice_nodo]
        try:
            self.conexion = pyodbc.connect(
                f"DRIVER={config['driver']};"
                f"SERVER={config['server']};"
                f"DATABASE={config['database']};"
                f"UID={config['username']};"
                f"PWD={config['password']}"
            )
            return True
        except Exception as e:
            print(f"❌ Error al conectar a {config['nombre']}: {e}")
            self.conexion = None
            return False

    def cambiar_nodo(self):
        """Cambia al otro nodo y reconecta."""
        self.indice_nodo = 1 - self.indice_nodo
        return self.conectar()


    def obtener_nodo_actual(self):
        """Devuelve el nombre del nodo actual."""
        return NODOS[self.indice_nodo]["nombre"]

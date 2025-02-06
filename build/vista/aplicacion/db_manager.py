import pyodbc
from config import NODOS
from build.vista.aplicacion import estado


class DatabaseManager:
    def __init__(self):
        self.conexion = None
        self.indice_nodo = self.obtener_indice_sede()
        self.conectar()

    def obtener_indice_sede(self):
        """Devuelve el índice del nodo actual basado en estado.SEDE_ACTUAL."""
        for i, nodo in enumerate(NODOS):
            if nodo["nombre"] == estado.SEDE_ACTUAL:
                return i
        return 0  # Si no encuentra la sede, usa la primera por defecto

    def conectar(self):
        """Conecta a la base de datos actual."""
        config = NODOS[self.indice_nodo]
        try:
            self.conexion = pyodbc.connect(
                f"DRIVER={config['driver']};"
                f"SERVER={config['server']};"
                f"DATABASE={config['database']};"
                f"UID={config['username']};"
                f"PWD={config['password']}"
            )
            print(f"✅ Conectado a {config['nombre']}")
            return True
        except Exception as e:
            print(f"❌ Error al conectar a {config['nombre']}: {e}")
            self.conexion = None
            return False

    def cambiar_nodo(self):
        """Cambia la sede en estado.py y reconecta."""
        estado.SEDE_ACTUAL = "Cuenca" if estado.SEDE_ACTUAL == "Quito" else "Quito"
        self.indice_nodo = self.obtener_indice_sede()
        return self.conectar()

    def obtener_nodo_actual(self):
        """Devuelve el nombre de la sede actual."""
        return estado.SEDE_ACTUAL

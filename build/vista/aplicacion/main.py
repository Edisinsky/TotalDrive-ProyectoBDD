from Inventario import window
import tkinter as tk
from DatabaseManager import DatabaseManager

# Instancia de la base de datos
db = DatabaseManager()

# Función para cambiar de nodo y actualizar la interfaz
def cambiar_nodo():
    if db.cambiar_nodo():
        estado_nodo.set(f"Conectado a: {db.obtener_nodo_actual()}")
    else:
        estado_nodo.set("❌ Error al conectar")

# Crear ventana
root = tk.Tk()
root.title("Cambio de Nodo SQL Server")
root.geometry("400x200")

estado_nodo = tk.StringVar()
estado_nodo.set(f"Conectado a: {db.obtener_nodo_actual()}")

resultado = tk.StringVar()
resultado.set("Presiona el botón para cambiar de nodo")

# Componentes de la UI
tk.Label(root, text="Estado:").pack(pady=5)
tk.Label(root, textvariable=estado_nodo, font=("Arial", 12, "bold")).pack()
tk.Button(root, text="Cambiar de Nodo", command=cambiar_nodo, font=("Arial", 12)).pack(pady=10)
tk.Label(root, textvariable=resultado, font=("Arial", 10)).pack()

if __name__ == "__main__":
    window.mainloop()



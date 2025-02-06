from pathlib import Path
from tkinter import ttk
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import tkinter as tk
from db_manager import DatabaseManager
import Inventario
import estado
import Vehiculo
import Servicio
import Reserva
import Mecanico
import Proveedor

def mostrar_ventana4():
    OUTPUT_PATH = Path(__file__).parent

    # Definir la ruta relativa a la carpeta de assets
    ASSETS_PATH = OUTPUT_PATH.parent / "assets" / "frame2"
    # Lista para almacenar los datos ingresados en los Entry
    datos_entrada = []

    def mostrar_mensaje(mensaje):
        """Muestra un mensaje en una ventana emergente."""
        ventana_mensaje = tk.Toplevel()
        ventana_mensaje.title("Mensaje")
        ventana_mensaje.geometry("400x150")

        # Obtener las dimensiones de la pantalla
        screen_width = ventana_mensaje.winfo_screenwidth()  # Ancho de la pantalla
        screen_height = ventana_mensaje.winfo_screenheight()  # Alto de la pantalla

        # Obtener las dimensiones de la ventana
        window_width = 400
        window_height = 150

        # Calcular la posición para centrar la ventana
        position_top = (screen_height // 2) - (window_height // 2)
        position_right = (screen_width // 2) - (window_width // 2)

        # Colocar la ventana en el centro de la pantalla
        ventana_mensaje.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

        etiqueta = tk.Label(ventana_mensaje, text=mensaje, font=("Arial", 12))
        etiqueta.pack(pady=30)

        boton_cerrar = tk.Button(ventana_mensaje, text="Cerrar", command=ventana_mensaje.destroy)
        boton_cerrar.pack()

        ventana_mensaje.mainloop()

    def agregar_texto():
        # Obtener valores de todas las entradas
        valores = [
            txt_cliente_id.get(),
            txt_nombre_cliente.get(),
            txt_correoCliente.get(),
            txt_telefono_cliente.get(),
        ]
        # Guardar en la lista
        datos_entrada.append(valores)
        print("Datos guardados:", datos_entrada)  # Mostrar en consola

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

     # Lista para almacenar los datos ingresados en los Entry
    datos_entrada = []
    db_manager=DatabaseManager()
    def agregar_texto():
        # Obtener valores de todas las entradas
        valores = [
            txt_cliente_id.get(),
            txt_nombre_cliente.get(),
            txt_correoCliente.get(),
            txt_telefono_cliente.get(),
        ]
        # Guardar en la lista
        datos_entrada.append(valores)
        print("Datos guardados:", datos_entrada)  # Mostrar en consola

    def abrir_inventario():
        window.destroy()
        Inventario.mostrar_ventana3()

    def abrir_vehiculo():
        window.destroy()
        Vehiculo.mostrar_ventana2()

    def abrir_servicio():
        window.destroy()
        Servicio.mostrar_ventana1()

    def abrir_reserva():
        window.destroy()
        Reserva.mostrar_ventana7()

    def abrir_mecanico():
        window.destroy()
        Mecanico.mostrar_ventana5()

    def abrir_proveedor():
        window.destroy()
        Proveedor.mostrar_ventana6()

    def insertarCliente(cliente_id, nombre_completo_cliente, correo_cliente, telefono_cliente):
        """Inserta un cliente en las tablas fragmentadas según su ubicación."""

        # Insertar en Quito (cliente_id y nombre_completo_cliente)
        nodo_actual = db_manager.obtener_nodo_actual()

        if nodo_actual != "Quito":
            db_manager.cambiar_nodo()  # Cambiar a Quito si no estamos en ese nodo

        consulta_quito = """
            INSERT INTO ClienteDatosBasicos (cliente_id, nombre_completo_cliente) 
            VALUES (?, ?)
        """
        resultado_quito = db_manager.ejecutar_consulta(consulta_quito, (cliente_id, nombre_completo_cliente))

        if "Error" in resultado_quito:
            mostrar_mensaje(f"❌ Error al insertar en Quito: {resultado_quito}")
            return  # Detener si hay error

        # Insertar en Cuenca (cliente_id, correo_cliente, telefono_cliente)
        db_manager.cambiar_nodo()  # Cambiar a Cuenca

        consulta_cuenca = """
            INSERT INTO ClienteDatosDeContacto (cliente_id, correo_cliente, telefono_cliente) 
            VALUES (?, ?, ?)
        """
        resultado_cuenca = db_manager.ejecutar_consulta(consulta_cuenca, (cliente_id, correo_cliente, telefono_cliente))

        if "Error" in resultado_cuenca:
            mostrar_mensaje(f"❌ Error al insertar en Cuenca")
            print(resultado_cuenca)
        else:
            mostrar_mensaje(f"✅ Cliente {nombre_completo_cliente} agregado con ID {cliente_id}")

        # Regresar al nodo inicial
        if nodo_actual != "Quito":
            db_manager.cambiar_nodo()

    def cambiar_sede():
        db_manager.cambiar_nodo()
        canvas.itemconfig(texto_sede, text=f"Sede:{estado.SEDE_ACTUAL}")

    def eliminarCliente(cliente_id):
        """Elimina un cliente de ambas tablas fragmentadas."""
        nodo_actual = db_manager.obtener_nodo_actual()

        # Eliminar en Quito (ClienteDatosBasicos)
        if nodo_actual != "Quito":
            db_manager.cambiar_nodo()

        consulta_quito = "DELETE FROM ClienteDatosBasicos WHERE cliente_id = ?"
        resultado_quito = db_manager.ejecutar_consulta(consulta_quito, (cliente_id,))

        if "Error" in resultado_quito:
            print(f"❌ Error al eliminar en Quito: {resultado_quito}")
            return  # Detener si hay error

        # Eliminar en Cuenca (ClienteDatosDeContacto)
        db_manager.cambiar_nodo()

        consulta_cuenca = "DELETE FROM ClienteDatosDeContacto WHERE cliente_id = ?"
        resultado_cuenca = db_manager.ejecutar_consulta(consulta_cuenca, (cliente_id,))

        if "Error" in resultado_cuenca:
            print(f"❌ Error al eliminar en Cuenca")
        else:
            print(f"✅ Cliente con ID {cliente_id} eliminado correctamente")

        # Regresar al nodo inicial
        if nodo_actual != "Quito":
            db_manager.cambiar_nodo()

    def limpiar_campos():
        """Limpia los campos de texto."""
        txt_cliente_id.delete(0, tk.END)
        txt_nombre_cliente.delete(0, tk.END)
        txt_correoCliente.delete(0, tk.END)
        txt_telefono_cliente.delete(0, tk.END)

    # Función para listar clientes según el nodo
    def listarClientes():
        """Muestra los clientes fragmentados según el nodo en el que se encuentre."""
        nodo_actual = db_manager.obtener_nodo_actual()

        if nodo_actual == "Quito":
            consulta = "SELECT * FROM ClienteDatosBasicos"
        else:
            consulta = "SELECT * FROM ClienteDatosDeContacto"

        resultado = db_manager.ejecutar_consulta(consulta)
        # Definir las columnas según el nodo
        if nodo_actual == "Quito":
            columnas = ("cliente_id", "nombre_completo_cliente")
            table_clientes = ttk.Treeview(window, columns=columnas, show="headings")
            table_clientes.heading("cliente_id", text="ID Cliente")
            table_clientes.heading("nombre_completo_cliente", text="Nombre Completo")
            table_clientes.column("cliente_id", width=100)
            table_clientes.column("nombre_completo_cliente", width=200)
        else:  # Nodo Cuenca
            columnas = ("cliente_id", "correo_cliente", "telefono_cliente")
            table_clientes = ttk.Treeview(window, columns=columnas, show="headings")
            table_clientes.heading("cliente_id", text="ID Cliente")
            table_clientes.heading("correo_cliente", text="Correo Electrónico")
            table_clientes.heading("telefono_cliente", text="Teléfono")
            table_clientes.column("cliente_id", width=100)
            table_clientes.column("correo_cliente", width=200)
            table_clientes.column("telefono_cliente", width=120)


        table_clientes.place(x=246.0, y=325.0, width=704.0, height=256.0)

        # Limpiar los datos previos
        table_clientes.delete(*table_clientes.get_children())

        # Insertar nuevos datos en la tabla de clientes
        if isinstance(resultado, list) and resultado:
            for fila in resultado:
                # Asegúrate de que cada valor sea una cadena y limpie los espacios
                fila_limpia = tuple(str(valor).strip() if valor is not None else "" for valor in fila)

                # Asignación de los valores a cada columna según la fragmentación:
                # Quito -> cliente_id, nombre_completo_cliente
                cliente_id = fila_limpia[0]
                nombre_completo = fila_limpia[1]  # Nombre completo
                apellido = fila_limpia[2] if len(fila_limpia) > 2 else ""  # Apellido (si está presente en Quito)

                # Cuenca -> correo_cliente, telefono_cliente
                correo_cliente = fila_limpia[3] if len(fila_limpia) > 3 else ""  # Correo de Cuenca
                telefono_cliente = fila_limpia[4] if len(fila_limpia) > 4 else ""  # Teléfono de Cuenca

                # Unir nombre y apellido para mostrar correctamente el nombre completo
                nombre_completo = f"{nombre_completo} {apellido}".strip()

                # Insertar en la tabla, asegurando que cada dato vaya a su columna correcta
                valores_finales = (cliente_id, nombre_completo, correo_cliente, telefono_cliente)
                table_clientes.insert("", "end", values=valores_finales)
        else:
            print("No se encontraron clientes.")

    def actualizarCliente(cliente_id, nuevo_nombre=None, nuevo_correo=None, nuevo_telefono=None):
        """Actualiza la información de un cliente en las tablas fragmentadas según el nodo correspondiente."""
        nodo_actual = db_manager.obtener_nodo_actual()

        # Si se proporciona un nuevo nombre, actualizar en Quito
        if nuevo_nombre:
            if nodo_actual != "Quito":
                db_manager.cambiar_nodo()  # Cambiar a Quito

            consulta_quito = """
                UPDATE ClienteDatosBasicos 
                SET nombre_completo_cliente = ? 
                WHERE cliente_id = ?
            """
            resultado_quito = db_manager.ejecutar_consulta(consulta_quito, (nuevo_nombre, cliente_id))

            if "Error" in resultado_quito:
                print(f"❌ Error al actualizar nombre en Quito: {resultado_quito}")
            else:
                print(f"✅ Nombre actualizado en Quito para el cliente {cliente_id}")

        # Si se proporciona nuevo correo o teléfono, actualizar en Cuenca
        if nuevo_correo or nuevo_telefono:
            db_manager.cambiar_nodo()  # Cambiar a Cuenca

            campos_a_actualizar = []
            valores = []

            if nuevo_correo:
                campos_a_actualizar.append("correo_cliente = ?")
                valores.append(nuevo_correo)
            if nuevo_telefono:
                campos_a_actualizar.append("telefono_cliente = ?")
                valores.append(nuevo_telefono)

            if campos_a_actualizar:
                consulta_cuenca = f"""
                    UPDATE ClienteDatosDeContacto 
                    SET {', '.join(campos_a_actualizar)}
                    WHERE cliente_id = ?
                """
                valores.append(cliente_id)
                resultado_cuenca = db_manager.ejecutar_consulta(consulta_cuenca, tuple(valores))

                if "Error" in resultado_cuenca:
                    print(f"❌ Error al actualizar datos de contacto en Cuenca")
                else:
                    print(f"✅ Datos de contacto actualizados en Cuenca para el cliente {cliente_id}")

        # Regresar al nodo inicial
        if nodo_actual != "Quito":
            db_manager.cambiar_nodo()

    window = Tk()

    window.geometry("987x617")
    window.configure(bg="#FFFFFF")

    # Obtener el ancho y alto de la pantalla
    screen_width = window.winfo_screenwidth()  # Ancho de la pantalla
    screen_height = window.winfo_screenheight()  # Alto de la pantalla

    # Calcular la posición x e y para centrar la ventana
    x_position = (screen_width // 2) - (987 // 2)  # Centrar horizontalmente
    y_position = (screen_height // 2) - (617 // 2)  # Centrar verticalmente

    # Establecer la posición de la ventana
    window.geometry(f"987x617+{x_position}+{y_position}")

    # Crear el Canvas
    canvas = Canvas(
        window,
        bg="#FFFFFF",
        height=617,
        width=987,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    canvas.place(x=0, y=0)

    # Dibujar un rectángulo en el Canvas
    canvas.create_rectangle(
        0.0,
        0.0,
        209.0,
        617.0,
        fill="#006DB2",
        outline=""
    )

    # BOTON 1 = SEDE
    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))

    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=cambiar_sede,
        relief="flat"
    )
    button_1.place(
        x=0.0,
        y=534.0,
        width=202.0,
        height=40.0
    )

    # CODIGO DE CLIENTE
    canvas.create_text(
        297.0,
        47.0,
        anchor="nw",
        text="Código de cliente: ",
        fill="#000000",
        font=("Inter", 13 * -1)
    )
    # Sede:X
    texto_sede=canvas.create_text(
        62.0,
        96.0,
        anchor="nw",
        text=f"Sede: {estado.SEDE_ACTUAL}",
        fill="#000000",
        font=("Inter", 13 * -1)
    )

    # Nombre de cliente
    canvas.create_text(
        293.0,
        98.0,
        anchor="nw",
        text="Nombre del cliente:",
        fill="#000000",
        font=("Inter", 13 * -1)
    )
    # Correo del cliente
    canvas.create_text(
        303.0000020414591,
        141.0,
        anchor="nw",
        text="Correo del cliente:",
        fill="#000000",
        font=("Inter", 13 * -1)
    )

    canvas.create_text(
        625.999971523881,
        47.0,
        anchor="nw",
        text="Teléfono del cliente:",
        fill="#000000",
        font=("Inter", 13 * -1)
    )
    # AGREGAR CLIENTE
    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: insertarCliente(txt_cliente_id.get(),txt_nombre_cliente.get(),txt_correoCliente.get(),txt_telefono_cliente.get()),
        relief="flat"
    )
    button_2.place(
        x=261.0,
        y=210.0,
        width=99.0,
        height=40.0
    )

    # ACTUALIZAR CLIENTE
    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: actualizarCliente(txt_cliente_id.get(), txt_nombre_cliente.get(), txt_correoCliente.get(), txt_telefono_cliente.get()),
        relief="flat"
    )
    button_3.place(
        x=540.0,
        y=210.0,
        width=113.0,
        height=40.0
    )
    # ELIMINAR CLIENTE
    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda :eliminarCliente(txt_cliente_id.get()),
        relief="flat"
    )
    button_4.place(
        x=688.0,
        y=210.0,
        width=100.0,
        height=40.0
    )
    # LISTAR CLIENTES
    button_image_5 = PhotoImage(
        file=relative_to_assets("button_5.png"))
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=listarClientes,
        relief="flat"
    )
    button_5.place(
        x=410.0,
        y=210.0,
        width=84.0,
        height=40.0
    )
    # LIMPIAR CAMPOS
    button_image_6 = PhotoImage(
        file=relative_to_assets("button_6.png"))
    button_6 = Button(
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=limpiar_campos,
        relief="flat"
    )
    button_6.place(
        x=828.0,
        y=210.0,
        width=96.0,
        height=40.0
    )

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        99.0,
        47.0,
        image=image_image_1
    )

    # Inventario
    button_image_7 = PhotoImage(
        file=relative_to_assets("button_7.png"))
    button_7 = Button(
        image=button_image_7,
        borderwidth=0,
        highlightthickness=0,
        command=abrir_inventario,
        relief="flat"
    )
    button_7.place(
        x=5.0,
        y=174.0,
        width=201.0,
        height=34.0
    )
    # cliente
    button_image_8 = PhotoImage(
        file=relative_to_assets("button_8.png"))
    button_8 = Button(
        image=button_image_8,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_8 clicked"),
        relief="flat"
    )
    button_8.place(
        x=5.0,
        y=275.0,
        width=201.0,
        height=34.0
    )
    # servicio
    button_image_9 = PhotoImage(
        file=relative_to_assets("button_9.png"))
    button_9 = Button(
        image=button_image_9,
        borderwidth=0,
        highlightthickness=0,
        command=abrir_servicio,
        relief="flat"
    )
    button_9.place(
        x=5.0,
        y=327.0,
        width=201.0,
        height=34.0
    )
    # RESERVA
    button_image_10 = PhotoImage(
        file=relative_to_assets("button_10.png"))
    button_10 = Button(
        image=button_image_10,
        borderwidth=0,
        highlightthickness=0,
        command=abrir_reserva,
        relief="flat"
    )
    button_10.place(
        x=5.0,
        y=376.0,
        width=201.0,
        height=34.0
    )
    # MECANICO
    button_image_11 = PhotoImage(
        file=relative_to_assets("button_11.png"))
    button_11 = Button(
        image=button_image_11,
        borderwidth=0,
        highlightthickness=0,
        command=abrir_mecanico,
        relief="flat"
    )
    button_11.place(
        x=5.0,
        y=421.0,
        width=201.0,
        height=34.0
    )
    # PROVEEDOR
    button_image_12 = PhotoImage(
        file=relative_to_assets("button_12.png"))
    button_12 = Button(
        image=button_image_12,
        borderwidth=0,
        highlightthickness=0,
        command=abrir_proveedor,
        relief="flat"
    )
    button_12.place(
        x=5.0,
        y=473.0,
        width=201.0,
        height=34.0
    )
    # VEHICULO
    button_image_13 = PhotoImage(
        file=relative_to_assets("button_13.png"))
    button_13 = Button(
        image=button_image_13,
        borderwidth=0,
        highlightthickness=0,
        command=abrir_vehiculo,
        relief="flat"
    )
    button_13.place(
        x=5.0,
        y=226.0,
        width=201.0,
        height=34.0
    )

    canvas.create_rectangle(
        248.0,
        327.0,
        952.0,
        583.0,
        fill="#15D1EE",
        outline="")

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        513.5,
        56.0,
        image=entry_image_1
    )
    # codigo de cliente
    txt_cliente_id = Entry(
        bd=0,
        bg="#A3CEEF",
        fg="#000716",
        highlightthickness=0
    )
    txt_cliente_id.place(
        x=443.0,
        y=43.0,
        width=141.0,
        height=24.0
    )
    # NOMBRE DEL CLIENTE
    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        513.5,
        107.0,
        image=entry_image_2
    )
    txt_nombre_cliente = Entry(
        bd=0,
        bg="#A3CEEF",
        fg="#000716",
        highlightthickness=0
    )
    txt_nombre_cliente.place(
        x=443.0,
        y=94.0,
        width=141.0,
        height=24.0
    )

    # CORREO DEL CLIENTE
    entry_image_3 = PhotoImage(
        file=relative_to_assets("entry_3.png"))
    entry_bg_3 = canvas.create_image(
        513.5,
        149.0,
        image=entry_image_3
    )
    txt_correoCliente = Entry(
        bd=0,
        bg="#A3CEEF",
        fg="#000716",
        highlightthickness=0
    )
    txt_correoCliente.place(
        x=443.0,
        y=136.0,
        width=141.0,
        height=24.0
    )

    # TELEFONO DEL CLIENTE
    entry_image_4 = PhotoImage(
        file=relative_to_assets("entry_4.png"))
    entry_bg_4 = canvas.create_image(
        840.5,
        56.0,
        image=entry_image_4
    )
    txt_telefono_cliente = Entry(
        bd=0,
        bg="#A3CEEF",
        fg="#000716",
        highlightthickness=0
    )
    txt_telefono_cliente.place(
        x=770.0,
        y=43.0,
        width=141.0,
        height=24.0
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        310.0,
        285.0,
        image=image_image_2
    )

    button_image_14 = PhotoImage(
        file=relative_to_assets("button_14.png"))
    button_14 = Button(
        image=button_image_14,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_14 clicked"),
        relief="flat"
    )
    button_14.place(
        x=376.0,
        y=271.0,
        width=217.0,
        height=34.0
    )

    # Determinar el nodo actual
    nodo_actual = db_manager.obtener_nodo_actual()



    window.resizable(False, False)
    window.mainloop()



from pathlib import Path

# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, ttk, Toplevel
import tkinter as tk
import estado
from db_manager import DatabaseManager
import Cliente
import Servicio
import Reserva
import Mecanico
import Proveedor
import Vehiculo


#############################
#creacion de funciones
#############################
def mostrar_mensaje(mensaje):
    """Muestra un mensaje en una ventana emergente."""
    ventana_mensaje = Toplevel()
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
def mostrar_ventana3():
    OUTPUT_PATH = Path(__file__).parent

    # Definir la ruta relativa a la carpeta de assets
    ASSETS_PATH = OUTPUT_PATH.parent / "assets" / "frame1"

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    def agregar_texto():
        valores = [
        txt_cod_repuesto.get(),
        txt_id_taller.get(),
        txt_prov.get(),
        txt_nombre_repuesto.get(),
        txt_cantidad_disponible.get()
        ]
        table.insert("", "end", values=valores)

    def abrir_vehiculo():
        window.destroy()
        Vehiculo.mostrar_ventana2()

    def abrir_cliente():

        window.destroy()
        Cliente.mostrar_ventana4()

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

    #############################
    # Funciones para la base de datos
    #############################
    # Crear la intancia del dba
    db_manager = DatabaseManager()

    def cambiar_sede():
        db_manager.cambiar_nodo()
        canvas.itemconfig(texto_sede, text=f"Sede:{estado.SEDE_ACTUAL}")

    def listarInventario():
        """Ejecuta una consulta SELECT en la base de datos actual mostrando la fragmentación correspondiente."""
        # Obtener el nodo actual
        nodo_actual = db_manager.obtener_nodo_actual()

        # Definir el ID de fragmentación según la sede
        id_taller = 1 if nodo_actual == "Quito" else 2  # Quito -> 1, Cuenca -> 2

        # Ejecutar la consulta filtrando por id_taller
        consulta = "SELECT * FROM Inventario WHERE id_taller = ?"
        resultado = db_manager.ejecutar_consulta(consulta, (id_taller))

        print=(f"📌 Inventario en la sede {nodo_actual}:", resultado)

        # Limpiar los datos previos de la tabla (si existen)
        for item in table.get_children():
            table.delete(item)

        # Verificar si hay resultados
        if isinstance(resultado, list) and len(resultado) > 0:
            # Insertar cada fila de resultados en la tabla
            for fila in resultado:
                # Asegurarse de que el nombre_repuesto no tenga un formato incorrecto
                cod_repuesto, id_taller, id_proveedor, nombre_repuesto, cantidad_disponible = fila
                nombre_repuesto = str(
                    nombre_repuesto).strip()  # Asegura que sea una cadena y limpia espacios innecesarios

                # Asegúrate de que todos los valores estén alineados correctamente con las columnas
                valores_fila = (cod_repuesto, id_taller, id_proveedor, nombre_repuesto, cantidad_disponible)
                table.insert("", "end", values=valores_fila)
        else:
            print("No se encontraron resultados.")




    def insertarInventario(cod_repuesto, id_taller, id_proveedor, nombre_repuesto, cantidad_disponible):
        """Inserta un nuevo repuesto en la tabla Inventario según la sede actual."""
        # Consulta SQL de inserción
        try:
            id_taller = int(id_taller)
        except ValueError:
            mensaje = "El id del taller debe ser un número entero"
            mostrar_mensaje(mensaje)
            return

        # Comparar después de asegurarnos que es un entero
        if id_taller > 2 or id_taller < 1:
            mensaje = "El id del taller no es válido"
            mostrar_mensaje(mensaje)
            return

        nodo_actual = db_manager.obtener_nodo_actual()
        consulta = """
            INSERT INTO Inventario (cod_repuesto, id_taller, id_proveedor, nombre_repuesto, cantidad_disponible)
            VALUES (?, ?, ?, ?, ?)
        """
        print(cod_repuesto, id_taller, id_proveedor, nombre_repuesto, cantidad_disponible)
        # Ejecutar la consulta con los parámetros
        resultado = db_manager.ejecutar_consulta(consulta, (
        cod_repuesto, id_taller, id_proveedor, nombre_repuesto, cantidad_disponible))

        if "Error" in resultado:
            mensaje = f"❌ Error al insertar en {nodo_actual}"
            print(resultado)
        else:
            mensaje = f"✅ Repuesto agregado a {nodo_actual}: {nombre_repuesto} con ID {cod_repuesto}"

        mostrar_mensaje(mensaje)




    def eliminarInventario(cod_repuesto, id_proveedor,id_taller):
        """Elimina un repuesto de la tabla Inventario según la sede actual."""
        nodo_actual = db_manager.obtener_nodo_actual()
        # Consulta SQL para eliminar el repuesto
        consulta = """
            set XACT_ABORT ON
            DELETE FROM Inventario
            WHERE cod_repuesto = ? AND id_proveedor = ? AND id_taller = ?
        """

        # Ejecutar la consulta con los parámetros
        resultado = db_manager.ejecutar_consulta(consulta, (
            cod_repuesto, id_proveedor, id_taller))

        if "Error" in resultado:
            mensaje=f"❌ Error al eliminar en {nodo_actual}"
            print(resultado)

        else:
            mensaje=f"✅ Repuesto con ID {cod_repuesto} eliminado de {nodo_actual}."
        mostrar_mensaje(mensaje)

    def actualizarInventario(cod_repuesto, id_proveedor, nombre_repuesto, cantidad_disponible,id_taller):
        """Actualiza un repuesto en la tabla Inventario según la sede actual."""
        nodo_actual = db_manager.obtener_nodo_actual()

        try:
            id_taller = int(id_taller)
        except ValueError:
            mensaje = "El id del taller debe ser un número entero"
            mostrar_mensaje(mensaje)
            return

        # Comparar después de asegurarnos que es un entero
        if id_taller > 2 or id_taller < 1:
            mensaje = "El id del taller no es válido"
            mostrar_mensaje(mensaje)
            return

        # Consulta SQL para actualizar el repuesto
        consulta = """
            set XACT_ABORT ON
            UPDATE Inventario
            SET nombre_repuesto = ?, cantidad_disponible = ?
            WHERE cod_repuesto = ? AND id_proveedor = ? AND id_taller = ?
        """

        # Ejecutar la consulta con los parámetros
        resultado = db_manager.ejecutar_consulta(consulta, (
            nombre_repuesto, cantidad_disponible, cod_repuesto, id_proveedor, id_taller))

        if "Error" in resultado:
            mensaje=f"❌ Error al actualizar en {nodo_actual}"
            print(resultado)

        else:
            mensaje=f"✅ Repuesto con ID {cod_repuesto} actualizado en {nodo_actual}."
        mostrar_mensaje(mensaje)

    def limpiar_campos():

        txt_cod_repuesto.delete(0, "end")
        txt_id_taller.delete(0, "end")
        txt_prov.delete(0, "end")
        txt_nombre_repuesto.delete(0, "end")
        txt_cantidad_disponible.delete(0, "end")

    def repuestos_stock_critico():
        """Consulta los repuestos con stock crítico según la sede actual."""
        # Obtener el nodo actual
        nodo_actual = db_manager.obtener_nodo_actual()

        consulta = """
                SELECT cod_repuesto, nombre_repuesto, cantidad_disponible
                FROM Inventario
                WHERE cantidad_disponible < 5;
            """

        # Ejecutar la consulta usando la función de ejecución del DBManager
        resultado = db_manager.ejecutar_consulta(consulta)

        # Limpiar la tabla antes de agregar nuevos datos
        for item in table.get_children():
            table.delete(item)

        if isinstance(resultado, list) and len(resultado) > 0:
            # Insertar cada fila de resultados en la tabla
            for fila in resultado:
                # Asegurarse de que el nombre_repuesto no tenga un formato incorrecto
                cod_repuesto, nombre_repuesto, cantidad_disponible = fila
                nombre_repuesto = str(
                    nombre_repuesto).strip()  # Asegura que sea una cadena y limpia espacios innecesarios

                # Asegúrate de que todos los valores estén alineados correctamente con las columnas
                valores_fila = (cod_repuesto, '-', '-', nombre_repuesto, cantidad_disponible)
                table.insert("", "end", values=valores_fila)

        return resultado


    #############################
    # Ventana
    #############################
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
    #############################
    # Interfaz
    #############################
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
    # SEDE
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
        x=2.0,
        y=526.0,
        width=202.0,
        height=40.0
    )

    canvas.create_text(
        297.0,
        47.0,
        anchor="nw",
        text="Código de repuesto: ",
        fill="#000000",
        font=("Inter", 13 * -1)
    )

    texto_sede = canvas.create_text(
        62.0,
        96.0,
        anchor="nw",
        text=f"Sede: {sede}",
        fill="#000000",
        font=("Inter", 13 * -1)
    )

    canvas.create_text(
        360.0,
        93.0,
        anchor="nw",
        text="Taller:",
        fill="#000000",
        font=("Inter", 13 * -1)
    )

    canvas.create_text(
        349.0000020414591,
        141.0,
        anchor="nw",
        text="Proveedor: ",
        fill="#000000",
        font=("Inter", 13 * -1)
    )

    canvas.create_text(
        614.999971523881,
        48.0,
        anchor="nw",
        text="Nombre del repuesto:",
        fill="#000000",
        font=("Inter", 13 * -1)
    )

    canvas.create_text(
        624.999971523881,
        94.0,
        anchor="nw",
        text="Cantidad disponible:",
        fill="#000000",
        font=("Inter", 13 * -1)
    )
    # AGREGAR REPUESTO
    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda :insertarInventario(txt_cod_repuesto.get(),txt_id_taller.get(), txt_prov.get(), txt_nombre_repuesto.get(), txt_cantidad_disponible.get()),
        relief="flat"
    )
    button_2.place(
        x=248.0,
        y=210.0,
        width=99.0,
        height=40.0
    )
    # ACTUALIZAR REPUESTO
    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: actualizarInventario(txt_cod_repuesto.get(),txt_prov.get(),txt_nombre_repuesto.get(),txt_cantidad_disponible.get(),txt_id_taller.get()),
        relief="flat"
    )
    button_3.place(
        x=512.0,
        y=210.0,
        width=113.0,
        height=40.0
    )
    # eliminar repuesto
    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: eliminarInventario(txt_cod_repuesto.get(),txt_prov.get(),txt_id_taller.get()),
        relief="flat"
    )
    button_4.place(
        x=664.0,
        y=210.0,
        width=100.0,
        height=40.0
    )

    # LISTAR
    button_image_5 = PhotoImage(
        file=relative_to_assets("button_5.png"))
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_5 clicked"),
        relief="flat"
    )
    button_5.place(
        x=383.0,
        y=210.0,
        width=84.0,
        height=40.0
    )
    # REPUESTOS CON STOCK CRITICO
    button_image_6 = PhotoImage(
        file=relative_to_assets("button_6.png"))
    button_6 = Button(
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=repuestos_stock_critico,
        relief="flat"
    )
    button_6.place(
        x=355.0,
        y=282.0,
        width=184.0,
        height=37.0
    )
    # CANTIDAD DISPONIBLE
    button_image_7 = PhotoImage(
        file=relative_to_assets("button_7.png"))
    button_7 = Button(
        image=button_image_7,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_7 clicked"),
        relief="flat"
    )
    button_7.place(
        x=583.0,
        y=285.0,
        width=155.0,
        height=32.0
    )
    # LIMPIAR CAMPOS
    button_image_8 = PhotoImage(
        file=relative_to_assets("button_8.png"))
    button_8 = Button(
        image=button_image_8,
        borderwidth=0,
        highlightthickness=0,
        command= limpiar_campos,
        relief="flat"
    )
    button_8.place(
        x=795.0,
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
    # INVENTARIO
    button_image_9 = PhotoImage(
        file=relative_to_assets("button_9.png"))
    button_9 = Button(
        image=button_image_9,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_9 clicked"),
        relief="flat"
    )
    button_9.place(
        x=5.0,
        y=174.0,
        width=201.0,
        height=34.0
    )
    # CLIENTE
    button_image_10 = PhotoImage(
        file=relative_to_assets("button_10.png"))
    button_10 = Button(
        image=button_image_10,
        borderwidth=0,
        highlightthickness=0,
        command=abrir_cliente,
        relief="flat"
    )
    button_10.place(
        x=5.0,
        y=275.0,
        width=201.0,
        height=34.0
    )
    # SERVICIO
    button_image_11 = PhotoImage(
        file=relative_to_assets("button_11.png"))
    button_11 = Button(
        image=button_image_11,
        borderwidth=0,
        highlightthickness=0,
        command=abrir_servicio,
        relief="flat"
    )
    button_11.place(
        x=5.0,
        y=327.0,
        width=201.0,
        height=34.0
    )
    # RESERVA
    button_image_12 = PhotoImage(
        file=relative_to_assets("button_12.png"))
    button_12 = Button(
        image=button_image_12,
        borderwidth=0,
        highlightthickness=0,
        command=abrir_reserva,
        relief="flat"
    )
    button_12.place(
        x=5.0,
        y=376.0,
        width=201.0,
        height=34.0
    )
    # MECANICO
    button_image_13 = PhotoImage(
        file=relative_to_assets("button_13.png"))
    button_13 = Button(
        image=button_image_13,
        borderwidth=0,
        highlightthickness=0,
        command=abrir_mecanico,
        relief="flat"
    )
    button_13.place(
        x=5.0,
        y=421.0,
        width=201.0,
        height=34.0
    )
    # PROVEEDOR
    button_image_14 = PhotoImage(
        file=relative_to_assets("button_14.png"))
    button_14 = Button(
        image=button_image_14,
        borderwidth=0,
        highlightthickness=0,
        command=abrir_proveedor,
        relief="flat"
    )
    button_14.place(
        x=5.0,
        y=470.0,
        width=201.0,
        height=34.0
    )
    # VEHICULO
    button_image_15 = PhotoImage(
        file=relative_to_assets("button_15.png"))
    button_15 = Button(
        image=button_image_15,
        borderwidth=0,
        highlightthickness=0,
        command=abrir_vehiculo,
        relief="flat"
    )
    button_15.place(
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
        fill="#007AFF",
        outline="")
    
    columns=("Codigo de repuesto","Taller","Proveedor","Nombre del repuesto","Cantidad disponible")
    table = ttk.Treeview(window, columns=columns, show='headings')
    table.heading("Codigo de repuesto", text="Codrepuesto")
    table.heading("Taller", text="Taller")
    table.heading("Proveedor", text="Proveedor")
    table.heading("Nombre del repuesto", text="NombreRepuesto")
    table.heading("Cantidad disponible", text="CantDisponible")
    # Ajustar Posicion
    table.column("Codigo de repuesto", anchor="center", width=50)
    table.column("Taller", anchor="center", width=50)
    table.column("Proveedor", anchor="center", width=100)
    table.column("Nombre del repuesto", anchor="center", width=200)
    table.column("Cantidad disponible", anchor="center", width=100)
    table.place(x=246.0, y=325.0, width=704.0, height=256.0)
    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        513.5,
        56.0,
        image=entry_image_1
    )
    
    
    txt_cod_repuesto = Entry(
        bd=0,
        bg="#A3CEEF",
        fg="#000716",
        highlightthickness=0
    )
    txt_cod_repuesto.place(
        x=443.0,
        y=43.0,
        width=141.0,
        height=24.0
    )
    # TALLER
    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        513.5,
        101.0,
        image=entry_image_2
    )
    txt_id_taller = Entry(
        bd=0,
        bg="#A3CEEF",
        fg="#000716",
        highlightthickness=0
    )

    txt_id_taller.place(
        x=443.0,
        y=88.0,
        width=141.0,
        height=24.0
    )
    # CANTIDAD DISPONIBLE
    entry_image_3 = PhotoImage(
        file=relative_to_assets("entry_3.png"))
    entry_bg_3 = canvas.create_image(
        798.0,
        102.0,
        image=entry_image_3
    )
    txt_cantidad_disponible = Entry(
        bd=0,
        bg="#A3CEEF",
        fg="#000716",
        highlightthickness=0
    )
    txt_cantidad_disponible.place(
        x=763.0,
        y=89.0,
        width=70.0,
        height=24.0
    )

    # PROVEEDOR
    entry_image_4 = PhotoImage(
        file=relative_to_assets("entry_4.png"))
    entry_bg_4 = canvas.create_image(
        513.5,
        149.0,
        image=entry_image_4
    )
    txt_prov = Entry(
        bd=0,
        bg="#A3CEEF",
        fg="#000716",
        highlightthickness=0
    )
    txt_prov.place(
        x=443.0,
        y=136.0,
        width=141.0,
        height=24.0
    )

    # NOMBRE DEL REPUESTO
    entry_image_5 = PhotoImage(
        file=relative_to_assets("entry_5.png"))
    entry_bg_5 = canvas.create_image(
        842.5,
        56.0,
        image=entry_image_5
    )
    txt_nombre_repuesto = Entry(
        bd=0,
        bg="#A3CEEF",
        fg="#000716",
        highlightthickness=0
    )
    valor = txt_nombre_repuesto.get()

    txt_nombre_repuesto.place(
        x=772.0,
        y=43.0,
        width=141.0,
        height=24.0
    )
    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        295.0,
        301.0,
        image=image_image_2
    )
    window.resizable(False, False)
    window.mainloop()

bool = True
if bool:
    mostrar_ventana3()
    bool = False
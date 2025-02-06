from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage
import Inventario
import Cliente
import Reserva
import Mecanico
import Proveedor
import Vehiculo

def mostrar_ventana1():
    OUTPUT_PATH = Path(__file__).parent

    # Definir la ruta relativa a la carpeta de assets
    ASSETS_PATH = OUTPUT_PATH.parent / "assets" / "frame3"

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)
    
    # Lista para almacenar los datos ingresados en los Entry
    datos_entrada = []

    def agregar_texto():
        # Obtener valores de todas las entradas
        valores = [
            entry_1.get(),
            entry_2.get(),
            entry_3.get(),
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

    def abrir_cliente():
        window.destroy()
        Cliente.mostrar_ventana4()
    def abrir_reserva():
        window.destroy()
        Reserva.mostrar_ventana7()
    def abrir_mecanico():
        window.destroy()
        Mecanico.mostrar_ventana5()
    def abrir_proveedor():
        window.destroy()
        Proveedor.mostrar_ventana6()
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
    canvas.create_rectangle(
        0.0,
        0.0,
        209.0,
        617.0,
        fill="#006DB2",
        outline="")

    canvas.create_text(
        285.0,
        47.0,
        anchor="nw",
        text="Código de servicio: ",
        fill="#000000",
        font=("Inter", 13 * -1)
    )

    canvas.create_text(
        62.0,
        96.0,
        anchor="nw",
        text="Sede: Quito",
        fill="#000000",
        font=("Inter", 13 * -1)
    )

    canvas.create_text(
        368.0,
        101.0,
        anchor="nw",
        text="Taller: ",
        fill="#000000",
        font=("Inter", 13 * -1)
    )

    canvas.create_text(
        625.999971523881,
        47.0,
        anchor="nw",
        text="Servicio:",
        fill="#000000",
        font=("Inter", 13 * -1)
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=agregar_texto,
        relief="flat"
    )
    button_1.place(
        x=279.0,
        y=210.0,
        width=99.0,
        height=40.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_2 clicked"),
        relief="flat"
    )
    button_2.place(
        x=543.0,
        y=210.0,
        width=113.0,
        height=40.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_3 clicked"),
        relief="flat"
    )
    button_3.place(
        x=701.0,
        y=211.0,
        width=100.0,
        height=40.0
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_4 clicked"),
        relief="flat"
    )
    button_4.place(
        x=416.0,
        y=210.0,
        width=84.0,
        height=40.0
    )

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
        x=839.0,
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

    button_image_6 = PhotoImage(
        file=relative_to_assets("button_6.png"))
    button_6 = Button(
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=abrir_inventario,
        relief="flat"
    )
    button_6.place(
        x=5.0,
        y=174.0,
        width=201.0,
        height=34.0
    )

    button_image_7 = PhotoImage(
        file=relative_to_assets("button_7.png"))
    button_7 = Button(
        image=button_image_7,
        borderwidth=0,
        highlightthickness=0,
        command=abrir_cliente,
        relief="flat"
    )
    button_7.place(
        x=5.0,
        y=275.0,
        width=201.0,
        height=34.0
    )

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
        y=327.0,
        width=201.0,
        height=34.0
    )

    button_image_9 = PhotoImage(
        file=relative_to_assets("button_9.png"))
    button_9 = Button(
        image=button_image_9,
        borderwidth=0,
        highlightthickness=0,
        command=abrir_reserva,
        relief="flat"
    )
    button_9.place(
        x=5.0,
        y=376.0,
        width=201.0,
        height=34.0
    )

    button_image_10 = PhotoImage(
        file=relative_to_assets("button_10.png"))
    button_10 = Button(
        image=button_image_10,
        borderwidth=0,
        highlightthickness=0,
        command=abrir_mecanico,
        relief="flat"
    )
    button_10.place(
        x=5.0,
        y=421.0,
        width=201.0,
        height=34.0
    )

    button_image_11 = PhotoImage(
        file=relative_to_assets("button_11.png"))
    button_11 = Button(
        image=button_image_11,
        borderwidth=0,
        highlightthickness=0,
        command=abrir_proveedor,
        relief="flat"
    )
    button_11.place(
        x=5.0,
        y=466.0,
        width=201.0,
        height=34.0
    )

    button_image_12 = PhotoImage(
        file=relative_to_assets("button_12.png"))
    button_12 = Button(
        image=button_image_12,
        borderwidth=0,
        highlightthickness=0,
        command=abrir_vehiculo,
        relief="flat"
    )
    button_12.place(
        x=5.0,
        y=226.0,
        width=201.0,
        height=34.0
    )

    canvas.create_rectangle(
        248.0,
        340.0,
        952.0,
        596.0,
        fill="#2EF193",
        outline="")

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        499.5,
        56.0,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#A3CEEF",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=429.0,
        y=43.0,
        width=141.0,
        height=24.0
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        499.5,
        109.0,
        image=entry_image_2
    )
    entry_2 = Entry(
        bd=0,
        bg="#A3CEEF",
        fg="#000716",
        highlightthickness=0
    )
    entry_2.place(
        x=429.0,
        y=96.0,
        width=141.0,
        height=24.0
    )

    entry_image_3 = PhotoImage(
        file=relative_to_assets("entry_3.png"))
    entry_bg_3 = canvas.create_image(
        776.5,
        56.0,
        image=entry_image_3
    )
    entry_3 = Entry(
        bd=0,
        bg="#A3CEEF",
        fg="#000716",
        highlightthickness=0
    )
    entry_3.place(
        x=706.0,
        y=43.0,
        width=141.0,
        height=24.0
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        303.0,
        299.0,
        image=image_image_2
    )

    button_image_13 = PhotoImage(
        file=relative_to_assets("button_13.png"))
    button_13 = Button(
        image=button_image_13,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_13 clicked"),
        relief="flat"
    )
    button_13.place(
        x=354.0,
        y=273.0,
        width=196.0,
        height=52.0
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
        x=0.0,
        y=527.0,
        width=202.0,
        height=40.0
    )
    window.resizable(False, False)
    window.mainloop()


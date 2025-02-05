from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import tkinter as tk
import Reserva

def mostrar_ventana8():
    OUTPUT_PATH = Path(__file__).parent

    # Definir la ruta relativa a la carpeta de assets
    ASSETS_PATH = OUTPUT_PATH.parent / "assets" / "frame7"

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)
    def agregar_texto():
        valores = [
        entry_1.get(),
        entry_2.get(),
        entry_3.get(),
        entry_4.get(),
        ]
        table.insert("", "end", values=valores)
    def abrir_reserva():
        window.destroy()
        Reserva.mostrar_ventana7()

    window = Tk()

    window.geometry("536x654")
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
    canvas.create_text(
        89.0,
        92.0,
        anchor="nw",
        text="Código de reserva: ",
        fill="#000000",
        font=("Inter", 13 * -1)
    )

    canvas.create_text(
        89.0,
        241.0,
        anchor="nw",
        text="Servicio Reservado",
        fill="#000000",
        font=("Inter", 13 * -1)
    )

    canvas.create_text(
        98.00003255903721,
        142.0,
        anchor="nw",
        text="Código Taller:",
        fill="#000000",
        font=("Inter", 13 * -1)
    )

    canvas.create_text(
        103.00003255903721,
        191.0,
        anchor="nw",
        text="Mecánico ID",
        fill="#000000",
        font=("Inter", 13 * -1)
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        303.5,
        101.0,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#A3CEEF",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=233.0,
        y=88.0,
        width=141.0,
        height=24.0
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        303.5,
        150.0,
        image=entry_image_2
    )
    entry_2 = Entry(
        bd=0,
        bg="#A3CEEF",
        fg="#000716",
        highlightthickness=0
    )
    entry_2.place(
        x=233.0,
        y=137.0,
        width=141.0,
        height=24.0
    )

    entry_image_3 = PhotoImage(
        file=relative_to_assets("entry_3.png"))
    entry_bg_3 = canvas.create_image(
        303.5,
        199.0,
        image=entry_image_3
    )
    entry_3 = Entry(
        bd=0,
        bg="#A3CEEF",
        fg="#000716",
        highlightthickness=0
    )
    entry_3.place(
        x=233.0,
        y=186.0,
        width=141.0,
        height=24.0
    )

    entry_image_4 = PhotoImage(
        file=relative_to_assets("entry_4.png"))
    entry_bg_4 = canvas.create_image(
        303.5,
        248.0,
        image=entry_image_4
    )
    entry_4 = Entry(
        bd=0,
        bg="#A3CEEF",
        fg="#000716",
        highlightthickness=0
    )
    entry_4.place(
        x=233.0,
        y=235.0,
        width=141.0,
        height=24.0
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )
    button_1.place(
        x=49.0,
        y=308.0,
        width=104.0,
        height=48.0
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
        x=258.0,
        y=312.0,
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
        x=387.0,
        y=312.0,
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
        x=164.0,
        y=312.0,
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
        x=219.0,
        y=370.0,
        width=96.0,
        height=40.0
    )

    canvas.create_rectangle(
        0.0,
        0.0,
        536.0,
        37.0,
        fill="#006DB2",
        outline="")
    
    column=("Código de reserva", "Código Taller", "Mecánico ID", "Servicio Reservado")
    table = tk.Treeview(window, columns=column, show='headings')
    table.heading("Código de reserva", text="Código de reserva")
    table.heading("Código Taller", text="Código Taller")
    table.heading("Mecánico ID", text="Mecánico ID")
    table.heading("Servicio Reservado", text="Servicio Reservado")
    table.place(x=0, y=420)
    #Posicion de la ventana
    table.column("Código de reserva", minwidth=0, width=150)
    table.column("Código Taller", minwidth=0, width=150)
    table.column("Mecánico ID", minwidth=0, width=150)
    table.column("Servicio Reservado", minwidth=0, width=150)


    button_image_6 = PhotoImage(
        file=relative_to_assets("button_6.png"))
    button_6 = Button(
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=abrir_reserva,
        relief="flat"
    )
    button_6.place(
        x=0.0,
        y=3.0,
        width=97.0,
        height=40.0
    )
    window.resizable(False, False)
    window.mainloop()


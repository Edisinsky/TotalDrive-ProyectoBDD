
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path


from build.service.MecanicoEntity import MecanicoEntity
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import subprocess

mecanicos = MecanicoEntity()
from build.vista.aplicacion.Inventario import btn_servicio

OUTPUT_PATH = Path(__file__).parent

# Definir la ruta relativa a la carpeta de assets
ASSETS_PATH = OUTPUT_PATH.parent /"assets" / "frame5"


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def abrir_inventario():
    subprocess.Popen(["python", "Inventario.py"])
    window.destroy()

def abrir_cliente():
    subprocess.Popen(["python", "Cliente.py"])
    window.destroy()

def abrir_servicio():
    subprocess.Popen(["python", "Servicio.py"])
    window.destroy()

def abrir_reserva():
    subprocess.Popen(["python", "Reserva.py"])
    window.destroy()

def abrir_proveedor():
    subprocess.Popen(["python", "Proveedor.py"])
    window.destroy()

def abrir_vehiculo():
    subprocess.Popen(["python", "Vehiculo.py"])
    window.destroy()

window = Tk()

window.geometry("987x617")
window.configure(bg = "#FFFFFF")


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
    x=2.0,
    y=526.0,
    width=202.0,
    height=40.0
)

canvas.create_text(
    267.0,
    50.0,
    anchor="nw",
    text="Código de mecánico: ",
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
    261.0,
    102.0,
    anchor="nw",
    text="Nombre del Mecánico:",
    fill="#000000",
    font=("Inter", 13 * -1)
)

canvas.create_text(
    667.999971523881,
    55.0,
    anchor="nw",
    text="Taller:",
    fill="#000000",
    font=("Inter", 13 * -1)
)

canvas.create_text(
    319.0000020414591,
    153.0,
    anchor="nw",
    text="Especialidad:",
    fill="#000000",
    font=("Inter", 13 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"), # Aqui se ubican las respectivas funciones
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
    x=279.0,
    y=210.0,
    width=99.0,
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
    x=543.0,
    y=210.0,
    width=113.0,
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
    x=701.0,
    y=211.0,
    width=100.0,
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
    x=423.0,
    y=212.0,
    width=84.0,
    height=40.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat"
)
button_6.place(
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

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=abrir_cliente,
    relief="flat"
)
button_8.place(
    x=5.0,
    y=275.0,
    width=201.0,
    height=34.0
)

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

button_image_11 = PhotoImage(
    file=relative_to_assets("button_11.png"))
button_11 = Button(
    image=button_image_11,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_11 clicked"),
    relief="flat"
)
button_11.place(
    x=5.0,
    y=421.0,
    width=201.0,
    height=34.0
)

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
    x=2.0,
    y=468.0,
    width=201.0,
    height=34.0
)

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
    340.0,
    952.0,
    596.0,
    fill="#FFC107",
    outline="")

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    499.5,
    58.0,
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
    y=45.0,
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
    499.5,
    162.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#A3CEEF",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=429.0,
    y=149.0,
    width=141.0,
    height=24.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    800.5,
    55.0,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#A3CEEF",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=730.0,
    y=42.0,
    width=141.0,
    height=24.0
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    302.0,
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
    x=358.0,
    y=269.0,
    width=303.0,
    height=31.0
)

button_image_15 = PhotoImage(
    file=relative_to_assets("button_15.png"))
button_15 = Button(
    image=button_image_15,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_15 clicked"),
    relief="flat"
)
button_15.place(
    x=698.0,
    y=270.0,
    width=187.0,
    height=28.0
)
window.resizable(False, False)
window.mainloop()

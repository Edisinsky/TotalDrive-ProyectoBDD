from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import subprocess

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH.parent / "assets" / "frame1"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def abrir_vehiculo():
    subprocess.Popen(["python", "Vehiculo.py"])
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

def abrir_mecanico():
    subprocess.Popen(["python", "Mecanico.py"])
    window.destroy()

def abrir_proveedor():
    subprocess.Popen(["python", "Proveedor.py"])
    window.destroy()

window = Tk()
window.geometry("987x617")
window.configure(bg="#FFFFFF")

# Centrar ventana
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x_position = (screen_width // 2) - (987 // 2)
y_position = (screen_height // 2) - (617 // 2)
window.geometry(f"987x617+{x_position}+{y_position}")

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

# Rectángulo lateral
canvas.create_rectangle(0.0, 0.0, 209.0, 617.0, fill="#006DB2", outline="")

# ================== CARGAR IMÁGENES ==================
button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
button_image_5 = PhotoImage(file=relative_to_assets("button_5.png"))
button_image_6 = PhotoImage(file=relative_to_assets("button_6.png"))
button_image_7 = PhotoImage(file=relative_to_assets("button_7.png"))
button_image_8 = PhotoImage(file=relative_to_assets("button_8.png"))
button_image_9 = PhotoImage(file=relative_to_assets("button_9.png"))
button_image_10 = PhotoImage(file=relative_to_assets("button_10.png"))
button_image_11 = PhotoImage(file=relative_to_assets("button_11.png"))
button_image_12 = PhotoImage(file=relative_to_assets("button_12.png"))
button_image_13 = PhotoImage(file=relative_to_assets("button_13.png"))
button_image_14 = PhotoImage(file=relative_to_assets("button_14.png"))
button_image_15 = PhotoImage(file=relative_to_assets("button_15.png"))

entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
entry_image_3 = PhotoImage(file=relative_to_assets("entry_3.png"))
entry_image_4 = PhotoImage(file=relative_to_assets("entry_4.png"))
entry_image_5 = PhotoImage(file=relative_to_assets("entry_5.png"))

image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))

# ================== BOTONES REFACTORIZADOS ==================
btn_sede = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("btn_sede clicked"),
    relief="flat"
)
btn_sede.place(x=2.0, y=526.0, width=202.0, height=40.0)

btn_agregar_repuesto = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("btn_agregar_repuesto clicked"),
    relief="flat"
)
btn_agregar_repuesto.place(x=248.0, y=210.0, width=99.0, height=40.0)

btn_actualizar_repuesto = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("btn_actualizar_repuesto clicked"),
    relief="flat"
)
btn_actualizar_repuesto.place(x=512.0, y=210.0, width=113.0, height=40.0)

btn_eliminar_repuesto = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("btn_eliminar_repuesto clicked"),
    relief="flat"
)
btn_eliminar_repuesto.place(x=664.0, y=210.0, width=100.0, height=40.0)

btn_listar = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("btn_listar clicked"),
    relief="flat"
)
btn_listar.place(x=383.0, y=210.0, width=84.0, height=40.0)

btn_filtro_stock_critico = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("btn_filtro_stock_critico clicked"),
    relief="flat"
)
btn_filtro_stock_critico.place(x=355.0, y=282.0, width=184.0, height=37.0)

btn_filtro_cantidad_disponible = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("btn_filtro_cantidad_disponible clicked"),
    relief="flat"
)
btn_filtro_cantidad_disponible.place(x=583.0, y=285.0, width=155.0, height=32.0)

btn_limpiar_campos = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("btn_limpiar_campos clicked"),
    relief="flat"
)
btn_limpiar_campos.place(x=795.0, y=210.0, width=96.0, height=40.0)

btn_inventario = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("btn_inventario clicked"),
    relief="flat"
)
btn_inventario.place(x=5.0, y=174.0, width=201.0, height=34.0)

btn_cliente = Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=abrir_cliente,
    relief="flat"
)
btn_cliente.place(x=5.0, y=275.0, width=201.0, height=34.0)

btn_servicio = Button(
    image=button_image_11,
    borderwidth=0,
    highlightthickness=0,
    command=abrir_servicio,
    relief="flat"
)
btn_servicio.place(x=5.0, y=327.0, width=201.0, height=34.0)

btn_reserva = Button(
    image=button_image_12,
    borderwidth=0,
    highlightthickness=0,
    command=abrir_reserva,
    relief="flat"
)
btn_reserva.place(x=5.0, y=376.0, width=201.0, height=34.0)

btn_mecanico = Button(
    image=button_image_13,
    borderwidth=0,
    highlightthickness=0,
    command=abrir_mecanico,
    relief="flat"
)
btn_mecanico.place(x=5.0, y=421.0, width=201.0, height=34.0)

btn_proveedor = Button(
    image=button_image_14,
    borderwidth=0,
    highlightthickness=0,
    command=abrir_proveedor,
    relief="flat"
)
btn_proveedor.place(x=5.0, y=470.0, width=201.0, height=34.0)

btn_vehiculo = Button(
    image=button_image_15,
    borderwidth=0,
    highlightthickness=0,
    command=abrir_vehiculo,
    relief="flat"
)
btn_vehiculo.place(x=5.0, y=226.0, width=201.0, height=34.0)

# ================== ENTRIES REFACTORIZADOS ==================
txt_codigo_repuesto = Entry(
    bd=0,
    bg="#A3CEEF",
    fg="#000716",
    highlightthickness=0
)
txt_codigo_repuesto.place(x=443.0, y=43.0, width=141.0, height=24.0)

txt_taller = Entry(
    bd=0,
    bg="#A3CEEF",
    fg="#000716",
    highlightthickness=0
)
txt_taller.place(x=443.0, y=88.0, width=141.0, height=24.0)

txt_cantidad_disponible = Entry(
    bd=0,
    bg="#A3CEEF",
    fg="#000716",
    highlightthickness=0
)
txt_cantidad_disponible.place(x=763.0, y=89.0, width=70.0, height=24.0)

txt_proveedor = Entry(
    bd=0,
    bg="#A3CEEF",
    fg="#000716",
    highlightthickness=0
)
txt_proveedor.place(x=443.0, y=136.0, width=141.0, height=24.0)

txt_nombre_repuesto = Entry(
    bd=0,
    bg="#A3CEEF",
    fg="#000716",
    highlightthickness=0
)
txt_nombre_repuesto.place(x=772.0, y=43.0, width=141.0, height=24.0)

# ================== ELEMENTOS DEL CANVAS ==================
canvas.create_image(99.0, 47.0, image=image_image_1)
canvas.create_image(295.0, 301.0, image=image_image_2)
canvas.create_rectangle(248.0, 327.0, 952.0, 583.0, fill="#007AFF", outline="")

# Textos del canvas
canvas.create_text(297.0, 47.0, anchor="nw", text="Código de repuesto: ", fill="#000000", font=("Inter", 13 * -1))
canvas.create_text(62.0, 96.0, anchor="nw", text="Sede: Quito", fill="#000000", font=("Inter", 13 * -1))
canvas.create_text(360.0, 93.0, anchor="nw", text="Taller:", fill="#000000", font=("Inter", 13 * -1))
canvas.create_text(349.0, 141.0, anchor="nw", text="Proveedor: ", fill="#000000", font=("Inter", 13 * -1))
canvas.create_text(615.0, 48.0, anchor="nw", text="Nombre del repuesto:", fill="#000000", font=("Inter", 13 * -1))
canvas.create_text(625.0, 94.0, anchor="nw", text="Cantidad disponible:", fill="#000000", font=("Inter", 13 * -1))

window.resizable(False, False)
window.mainloop()
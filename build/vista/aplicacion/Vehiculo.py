
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent

# Definir la ruta relativa a la carpeta de assets
ASSETS_PATH = OUTPUT_PATH.parent /"assets" / "frame0"


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("987x617")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 617,
    width = 987,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    209.0,
    617.0,
    fill="#006DB2",
    outline="")

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
    62.0,
    96.0,
    anchor="nw",
    text="Sede: Quito",
    fill="#000000",
    font=("Inter", 13 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    513.5,
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
    x=443.0,
    y=43.0,
    width=141.0,
    height=24.0
)

canvas.create_text(
    362.0,
    49.0,
    anchor="nw",
    text="Modelo: ",
    fill="#000000",
    font=("Inter", 13 * -1)
)

canvas.create_text(
    365.0,
    91.0,
    anchor="nw",
    text="Marca:",
    fill="#000000",
    font=("Inter", 13 * -1)
)

canvas.create_text(
    353.0000020414591,
    128.0,
    anchor="nw",
    text="Propietario: ",
    fill="#000000",
    font=("Inter", 13 * -1)
)

canvas.create_text(
    610.999971523881,
    48.0,
    anchor="nw",
    text="Placa:",
    fill="#000000",
    font=("Inter", 13 * -1)
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
    x=248.0,
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
    x=512.0,
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
    x=664.0,
    y=210.0,
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
    x=383.0,
    y=210.0,
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
    command=lambda: print("button_8 clicked"),
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
    command=lambda: print("button_9 clicked"),
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
    command=lambda: print("button_10 clicked"),
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
    command=lambda: print("button_12 clicked"),
    relief="flat"
)
button_12.place(
    x=5.0,
    y=473.0,
    width=201.0,
    height=34.0
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
    fill="#7879F1",
    outline="")

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    513.5,
    56.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#A3CEEF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=443.0,
    y=43.0,
    width=141.0,
    height=24.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    512.5,
    97.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#A3CEEF",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=442.0,
    y=84.0,
    width=141.0,
    height=24.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    511.5,
    141.0,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#A3CEEF",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=441.0,
    y=128.0,
    width=141.0,
    height=24.0
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    741.5,
    58.0,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#A3CEEF",
    fg="#000716",
    highlightthickness=0
)
entry_5.place(
    x=671.0,
    y=45.0,
    width=141.0,
    height=24.0
)
window.resizable(False, False)
window.mainloop()
#hola
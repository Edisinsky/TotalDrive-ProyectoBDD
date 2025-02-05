import tkinter as tk
from tkinter import PhotoImage
from pathlib import Path


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestión de Taller")
        self.geometry("987x617")
        self.configure(bg="#FFFFFF")
        self.resizable(False, False)

        self.frames = {}
        for F in (Cliente, Inventario, Vehiculo, Servicio, Reserva, Mecanico, Proveedor):
            page_name = F.__name__
            frame = F(parent=self, controller=self)
            self.frames[page_name] = frame
            frame.place(x=0, y=0, relwidth=1, relheight=1)

        self.show_frame("Inventario")

    def show_frame(self, page_name):
        print(f"Cambiando a {page_name}")  # Depuración
        frame = self.frames.get(page_name)
        if frame:
            frame.tkraise()
        else:
            print(f"Error: {page_name} no encontrado en self.frames")


class BaseFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg="#FFFFFF")
        self.create_widgets()

    def create_widgets(self):
        pass

    def create_nav_buttons(self, buttons):
        for (x, y, text, target) in buttons:
            btn = tk.Button(self, text=text, command=lambda t=target: self.controller.show_frame(t))
            btn.place(x=x, y=y, width=150, height=40)


class Cliente(BaseFrame):
    def create_widgets(self):
        self.create_nav_buttons([
            (5, 174, "Inventario", "Inventario"),
            (5, 226, "Vehículo", "Vehiculo"),
            (5, 327, "Servicio", "Servicio"),
            (5, 376, "Reserva", "Reserva"),
            (5, 421, "Mecánico", "Mecanico"),
            (5, 473, "Proveedor", "Proveedor")
        ])


class Inventario(BaseFrame):
    def create_widgets(self):
        self.create_nav_buttons([
            (5, 174, "Vehículo", "Vehiculo"),
            (5, 226, "Cliente", "Cliente"),
            (5, 327, "Servicio", "Servicio"),
            (5, 376, "Reserva", "Reserva"),
            (5, 421, "Mecánico", "Mecanico"),
            (5, 473, "Proveedor", "Proveedor")
        ])


class Vehiculo(BaseFrame):
    def create_widgets(self):
        self.create_nav_buttons([
            (5, 174, "Inventario", "Inventario"),
            (5, 226, "Cliente", "Cliente"),
            (5, 327, "Servicio", "Servicio"),
            (5, 376, "Reserva", "Reserva"),
            (5, 421, "Mecánico", "Mecanico"),
            (5, 473, "Proveedor", "Proveedor")
        ])


class Servicio(BaseFrame):
    def create_widgets(self):
        self.create_nav_buttons([
            (5, 174, "Inventario", "Inventario"),
            (5, 226, "Vehículo", "Vehiculo"),
            (5, 327, "Cliente", "Cliente"),
            (5, 376, "Reserva", "Reserva"),
            (5, 421, "Mecánico", "Mecanico"),
            (5, 473, "Proveedor", "Proveedor")
        ])


class Reserva(BaseFrame):
    def create_widgets(self):
        self.create_nav_buttons([
            (5, 174, "Inventario", "Inventario"),
            (5, 226, "Vehículo", "Vehiculo"),
            (5, 327, "Cliente", "Cliente"),
            (5, 376, "Servicio", "Servicio"),
            (5, 421, "Mecánico", "Mecanico"),
            (5, 473, "Proveedor", "Proveedor")
        ])


class Mecanico(BaseFrame):
    def create_widgets(self):
        self.create_nav_buttons([
            (5, 174, "Inventario", "Inventario"),
            (5, 226, "Cliente", "Cliente"),
            (5, 327, "Servicio", "Servicio"),
            (5, 376, "Reserva", "Reserva"),
            (5, 473, "Proveedor", "Proveedor"),
            (5, 421, "Vehículo", "Vehiculo")
        ])


class Proveedor(BaseFrame):
    def create_widgets(self):
        self.create_nav_buttons([
            (5, 174, "Inventario", "Inventario"),
            (5, 226, "Vehículo", "Vehiculo"),
            (5, 327, "Cliente", "Cliente"),
            (5, 376, "Servicio", "Servicio"),
            (5, 421, "Reserva", "Reserva"),
            (5, 473, "Mecánico", "Mecanico")
        ])


if __name__ == "__main__":
    app = App()
    app.mainloop()

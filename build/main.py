# import pyodbc
# from tkinter import Tk, Canvas, Entry, Button, messagebox
#
#
# # ----------------- CONEXIÓN A SQL SERVER -----------------
# def conectar_bd():
#     try:
#         conn = pyodbc.connect(
#             "DRIVER={SQL Server};"
#             "SERVER=CHESCO;"  # Cambia esto con el nombre de tu servidor
#             "DATABASE=TallerQuito;"  # Cambia esto con tu base de datos
#             "UID=quito;"  # Usuario si usas autenticación de SQL Server
#             "PWD=1234;"  # Contraseña
#             "Trusted_Connection=no"  # Usa "yes" si es autenticación de Windows
#         )
#         return conn
#     except Exception as e:
#         messagebox.showerror("Error de conexión", f"No se pudo conectar a SQL Server: {e}")
#         return None
#
#
# # ----------------- FUNCIONES CRUD -----------------
# def insertar_cliente():
#     id_cliente = entry_codigo.get()
#     nombre = entry_nombre.get()
#     correo = entry_correo.get()
#     telefono = entry_telefono.get()
#
#     if not id_cliente or not nombre or not correo or not telefono:
#         messagebox.showwarning("Campos vacíos", "Todos los campos son obligatorios")
#         return
#
#     try:
#         conn = conectar_bd()
#         cursor = conn.cursor()
#         consulta = "INSERT INTO CLIENTE (ID_CLIENTE, NOMBRE_CLIENTE, CORREO_CLIENTE, TELEFONO_CLIENTE) VALUES (?, ?, ?, ?)"
#         cursor.execute(consulta, (id_cliente, nombre, correo, telefono))
#         conn.commit()
#         conn.close()
#         messagebox.showinfo("Éxito", "Cliente agregado correctamente")
#         limpiar_campos()
#     except Exception as e:
#         messagebox.showerror("Error", f"Error al insertar cliente: {e}")
#
#
# def actualizar_cliente():
#     id_cliente = entry_codigo.get()
#     nombre = entry_nombre.get()
#     correo = entry_correo.get()
#     telefono = entry_telefono.get()
#
#     if not id_cliente:
#         messagebox.showwarning("Campos vacíos", "El Código de Cliente es obligatorio para actualizar")
#         return
#
#     try:
#         conn = conectar_bd()
#         cursor = conn.cursor()
#         consulta = "UPDATE CLIENTE SET NOMBRE_CLIENTE = ?, CORREO_CLIENTE = ?, TELEFONO_CLIENTE = ? WHERE ID_CLIENTE = ?"
#         cursor.execute(consulta, (nombre, correo, telefono, id_cliente))
#         conn.commit()
#         conn.close()
#         messagebox.showinfo("Éxito", "Cliente actualizado correctamente")
#         limpiar_campos()
#     except Exception as e:
#         messagebox.showerror("Error", f"Error al actualizar cliente: {e}")
#
#
# def eliminar_cliente():
#     id_cliente = entry_codigo.get()
#
#     if not id_cliente:
#         messagebox.showwarning("Campos vacíos", "El Código de Cliente es obligatorio para eliminar")
#         return
#
#     try:
#         conn = conectar_bd()
#         cursor = conn.cursor()
#         consulta = "DELETE FROM CLIENTE WHERE ID_CLIENTE = ?"
#         cursor.execute(consulta, (id_cliente,))
#         conn.commit()
#         conn.close()
#         messagebox.showinfo("Éxito", "Cliente eliminado correctamente")
#         limpiar_campos()
#     except Exception as e:
#         messagebox.showerror("Error", f"Error al eliminar cliente: {e}")
#
#
# def limpiar_campos():
#     entry_codigo.delete(0, "end")
#     entry_nombre.delete(0, "end")
#     entry_correo.delete(0, "end")
#     entry_telefono.delete(0, "end")
#
#
# # # ----------------- INTERFAZ GRÁFICA -----------------
# # window = Tk()
# # window.geometry("600x400")
# # window.title("Gestión de Clientes")
# #
# # canvas = Canvas(window, bg="#FFFFFF", height=400, width=600)
# # canvas.pack()
# #
# # canvas.create_text(50, 50, anchor="nw", text="Código de Cliente:", font=("Inter", 12))
# # entry_codigo = Entry(window)
# # entry_codigo.place(x=200, y=50, width=200)
# #
# # canvas.create_text(50, 100, anchor="nw", text="Nombre:", font=("Inter", 12))
# # entry_nombre = Entry(window)
# # entry_nombre.place(x=200, y=100, width=200)
# #
# # canvas.create_text(50, 150, anchor="nw", text="Correo:", font=("Inter", 12))
# # entry_correo = Entry(window)
# # entry_correo.place(x=200, y=150, width=200)
# #
# # canvas.create_text(50, 200, anchor="nw", text="Teléfono:", font=("Inter", 12))
# # entry_telefono = Entry(window)
# # entry_telefono.place(x=200, y=200, width=200)
# #
# # btn_insertar = Button(window, text="Insertar", command=insertar_cliente)
# # btn_insertar.place(x=50, y=300, width=100)
# #
# # btn_actualizar = Button(window, text="Actualizar", command=actualizar_cliente)
# # btn_actualizar.place(x=160, y=300, width=100)
# #
# # btn_eliminar = Button(window, text="Eliminar", command=eliminar_cliente)
# # btn_eliminar.place(x=270, y=300, width=100)
# #
# # btn_limpiar = Button(window, text="Limpiar", command=limpiar_campos)
# # btn_limpiar.place(x=380, y=300, width=100)
# #
# # window.mainloop()

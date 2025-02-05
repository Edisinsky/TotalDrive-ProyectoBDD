

class ProveedorEntity:
    def __init__(self, db: Session):
        self.db = db

    def crear_proveedor(self, nombre: str, telefono: str, email: str):
        nuevo_proveedor = Proveedor(nombre_proveedor=nombre, telefono_proveedor=telefono, email_proveedor=email)
        self.db.add(nuevo_proveedor)
        self.db.commit()
        self.db.refresh(nuevo_proveedor)
        return nuevo_proveedor

    def obtener_proveedores(self):
        return self.db.query(Proveedor).all()

    def actualizar_proveedor(self, proveedor_id: int, nombre: str = None, telefono: str = None, email: str = None):
        proveedor = self.db.query(Proveedor).filter(Proveedor.proveedor_id == proveedor_id).first()
        if proveedor:
            if nombre:
                proveedor.nombre_proveedor = nombre
            if telefono:
                proveedor.telefono_proveedor = telefono
            if email:
                proveedor.email_proveedor = email
            self.db.commit()
            self.db.refresh(proveedor)
        return proveedor

    def eliminar_proveedor(self, proveedor_id: int):
        proveedor = self.db.query(Proveedor).filter(Proveedor.proveedor_id == proveedor_id).first()
        if proveedor:
            self.db.delete(proveedor)
            self.db.commit()
        return proveedor

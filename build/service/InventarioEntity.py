

class InventarioEntity:
    def __init__(self, db: Session):
        self.db = db

    def crear_inventario(self, id_taller: int, id_proveedor: int, nombre_repuesto: str, cantidad_disponible: int):
        nuevo_inventario = Inventario(id_taller=id_taller, id_proveedor=id_proveedor, nombre_repuesto=nombre_repuesto, cantidad_disponible=cantidad_disponible)
        self.db.add(nuevo_inventario)
        self.db.commit()
        self.db.refresh(nuevo_inventario)
        return nuevo_inventario

    def obtener_inventarios(self):
        return self.db.query(Inventario).all()

    def actualizar_inventario(self, cod_repuesto: int, nombre_repuesto: str = None, cantidad_disponible: int = None):
        inventario = self.db.query(Inventario).filter(Inventario.cod_repuesto == cod_repuesto).first()
        if inventario:
            if nombre_repuesto:
                inventario.nombre_repuesto = nombre_repuesto
            if cantidad_disponible is not None:
                inventario.cantidad_disponible = cantidad_disponible
            self.db.commit()
            self.db.refresh(inventario)
        return inventario

    def eliminar_inventario(self, cod_repuesto: int):
        inventario = self.db.query(Inventario).filter(Inventario.cod_repuesto == cod_repuesto).first()
        if inventario:
            self.db.delete(inventario)
            self.db.commit()
        return inventario
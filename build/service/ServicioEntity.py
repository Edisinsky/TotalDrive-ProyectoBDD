

class ServicioEntity:
    def __init__(self, db: Session):
        self.db = db

    def crear_servicio(self, id_taller: int, servicio: str):
        nuevo_servicio = Servicio(id_taller=id_taller, servicio=servicio)
        self.db.add(nuevo_servicio)
        self.db.commit()
        self.db.refresh(nuevo_servicio)
        return nuevo_servicio

    def obtener_servicios(self):
        return self.db.query(Servicio).all()

    def actualizar_servicio(self, id_servicio: int, servicio: str = None):
        servicio_obj = self.db.query(Servicio).filter(Servicio.id_servicio == id_servicio).first()
        if servicio_obj:
            if servicio:
                servicio_obj.servicio = servicio
            self.db.commit()
            self.db.refresh(servicio_obj)
        return servicio_obj

    def eliminar_servicio(self, id_servicio: int):
        servicio = self.db.query(Servicio).filter(Servicio.id_servicio == id_servicio).first()
        if servicio:
            self.db.delete(servicio)
            self.db.commit()
        return servicio

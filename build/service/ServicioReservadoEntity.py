

class ServicioReservadoEntity:
    def __init__(self, db: Session):
        self.db = db

    def crear_servicio_reservado(self, reserva_id: int, mecanico_id: int, servicio_reservado: str):
        nuevo_servicio_reservado = ServicioReservado(reserva_id=reserva_id, mecanico_id=mecanico_id, servicio_reservado=servicio_reservado)
        self.db.add(nuevo_servicio_reservado)
        self.db.commit()
        self.db.refresh(nuevo_servicio_reservado)
        return nuevo_servicio_reservado

    def obtener_servicios_reservados(self):
        return self.db.query(ServicioReservado).all()

    def actualizar_servicio_reservado(self, reserva_id: int, mecanico_id: int = None, servicio_reservado: str = None):
        servicio_reservado_obj = self.db.query(ServicioReservado).filter(ServicioReservado.reserva_id == reserva_id).first()
        if servicio_reservado_obj:
            if mecanico_id is not None:
                servicio_reservado_obj.mecanico_id = mecanico_id
            if servicio_reservado is not None:
                servicio_reservado_obj.servicio_reservado = servicio_reservado
            self.db.commit()
            self.db.refresh(servicio_reservado_obj)
        return servicio_reservado_obj

    def eliminar_servicio_reservado(self, reserva_id: int):
        servicio_reservado = self.db.query(ServicioReservado).filter(ServicioReservado.reserva_id == reserva_id).first()
        if servicio_reservado:
            self.db.delete(servicio_reservado)
            self.db.commit()
        return servicio_reservado




class ReservaEntity:
    def __init__(self, db: Session):
        self.db = db

    def crear_reserva(self, vehiculo_placa: str, id_taller: int, FechaReserva: str, Estado: str):
        nueva_reserva = Reserva(vehiculo_placa=vehiculo_placa, id_taller=id_taller, FechaReserva=FechaReserva, Estado=Estado)
        self.db.add(nueva_reserva)
        self.db.commit()
        self.db.refresh(nueva_reserva)
        return nueva_reserva

    def obtener_reservas(self):
        return self.db.query(Reserva).all()

    def actualizar_reserva(self, reserva_id: int, FechaReserva: str = None, Estado: str = None):
        reserva = self.db.query(Reserva).filter(Reserva.reserva_id == reserva_id).first()
        if reserva:
            if FechaReserva:
                reserva.FechaReserva = FechaReserva
            if Estado:
                reserva.Estado = Estado
            self.db.commit()
            self.db.refresh(reserva)
        return reserva

    def eliminar_reserva(self, reserva_id: int):
        reserva = self.db.query(Reserva).filter(Reserva.reserva_id == reserva_id).first()
        if reserva:
            self.db.delete(reserva)
            self.db.commit()
        return reserva
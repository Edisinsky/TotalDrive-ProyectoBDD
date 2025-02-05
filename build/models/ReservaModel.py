from build.models.Base import Base

class Reserva(Base):
    __tablename__ = 'Reserva'

    reserva_id = Column(Integer)
    vehiculo_placa = Column(String(15))
    id_taller = Column(Integer)
    FechaReserva = Column()
    nombre_completo_cliente = Column(String(150))

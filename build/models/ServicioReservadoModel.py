from sqlalchemy import Column, Integer, String, ForeignKey, DATETIME
from build.models.Base import Base

class ServicioReservado(Base):
    __tablename__ = 'servicio_reservado'

    reserva_id = Column(Integer, ForeignKey('reserva.reserva_id'), primary_key=True)
    mecanico_id = Column(Integer, nullable=False)
    servicio_reservado = Column(String, nullable=False)
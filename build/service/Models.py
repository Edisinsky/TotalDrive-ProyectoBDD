from sqlalchemy import Column, Integer, String, ForeignKey, DATETIME
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class ReservaCuenca(Base):
    __tablename__ = 'ReservaCuenca'

    reserva_id = Column(Integer)
    vehiculo_placa = Column(String(15))
    id_taller = Column(Integer)
    FechaReserva = Column()
    nombre_completo_cliente = Column(String(150))

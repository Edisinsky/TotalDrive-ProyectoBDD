from sqlalchemy import Column, Integer, String, ForeignKey, DATETIME
from build.models.Base import Base

class Vehiculo(Base):
    __tablename__ = 'vehiculo'

    placa = Column(String, primary_key=True)
    id_propietario = Column(Integer, nullable=False)
    modelo = Column(String, nullable=False)
    marca = Column(String, nullable=False)
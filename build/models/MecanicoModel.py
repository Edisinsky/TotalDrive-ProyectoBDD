from sqlalchemy import Column, Integer, String, ForeignKey, DATETIME, Identity
from build.models.Base import Base

class Mecanico(Base):
    __tablename__ = 'Mecanico'
    __table_args__ = {"schema": "dbo"}
    mecanico_id = Column(Integer,primary_key=True)
    id_taller = Column(Integer, nullable=False)
    especialidad = Column(String, nullable=False)
    nombre_completo_mecanico = Column(String, nullable=False)


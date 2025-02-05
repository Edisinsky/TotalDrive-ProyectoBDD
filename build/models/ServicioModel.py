from sqlalchemy import Column, Integer, String, ForeignKey, DATETIME
from build.models.Base import Base

class Servicio(Base):
    __tablename__ = 'servicio'

    id_servicio = Column(Integer, primary_key=True, autoincrement=True)
    id_taller = Column(Integer, nullable=False)
    servicio = Column(String, nullable=False)

from sqlalchemy import Column, Integer, String, ForeignKey, DATETIME, Table, MetaData
from build.models.Base import Base
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker


class Mecanico(Base):
    __tablename__ = 'Mecanico'

    mecanico_id = Column(Integer,primary_key=True)
    id_taller = Column(Integer, nullable=False)
    especialidad = Column(String, nullable=False)
    nombre_completo_mecanico = Column(String, nullable=False)

from sqlalchemy import Column, Integer, String, ForeignKey, DATETIME
from build.models.Base import Base

class Cliente(Base):
    __tablename__ = 'Cliente'

    cliente_id = Column( "cliente_id", Integer, primary_key=True)
    telefono_cliente = Column("telefono_cliente",String)
    correo_cliente = Column("correo_cliente",String)
    nombre_completo_cliente = Column( "nombre_completo_cliente", String(150))
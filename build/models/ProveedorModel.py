from sqlalchemy import Column, Integer, String, ForeignKey, DATETIME
from build.models.Base import Base
from sqlalchemy.orm import relationship


class Proveedor(Base):
    __tablename__ = 'proveedor'

    proveedor_id = Column(Integer, primary_key=True, autoincrement=True)
    nombre_proveedor = Column(String, nullable=False)
    telefono_proveedor = Column(String, nullable=True)
    email_proveedor = Column(String, nullable=True)

    inventarios = relationship("Inventario", back_populates="proveedor")
from sqlalchemy import Column, Integer, String, ForeignKey, DATETIME
from sqlalchemy.orm import relationship

from build.models.Base import Base


class Inventario(Base):
    __tablename__ = 'inventario'

    cod_repuesto = Column(Integer, primary_key=True, autoincrement=True)
    id_taller = Column(Integer, nullable=False)
    id_proveedor = Column(Integer, ForeignKey('proveedor.proveedor_id'))
    nombre_repuesto = Column(String, nullable=False)
    cantidad_disponible = Column(Integer, nullable=False)

    proveedor = relationship("Proveedor", back_populates="inventarios")

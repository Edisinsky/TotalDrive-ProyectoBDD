from sqlalchemy.orm import Session
from build.models.MecanicoModel import Mecanico
from build.service.ConexionQuito import get_db


class MecanicoEntity:

    @staticmethod
    def crear_mecanico(mecanico_id: int,id_taller: int, especialidad: str, nombre_completo_mecanico: str):
        db = next(get_db())
        nuevo_mecanico = Mecanico(mecanico_id=mecanico_id,id_taller=id_taller, especialidad=especialidad, nombre_completo_mecanico=nombre_completo_mecanico)
        db.add(nuevo_mecanico)
        db.commit()
        db.refresh(nuevo_mecanico)
        return nuevo_mecanico

    def obtener_mecanicos(self):
        return self.db.query(Mecanico).all()

    def actualizar_mecanico(self, mecanico_id: int, especialidad: str = None, nombre_completo_mecanico: str = None):
        mecanico = self.db.query(Mecanico).filter(Mecanico.mecanico_id == mecanico_id).first()
        if mecanico:
            if especialidad is not None:
                mecanico.especialidad = especialidad
            if nombre_completo_mecanico is not None:
                mecanico.nombre_completo_mecanico = nombre_completo_mecanico
            self.db.commit()
            self.db.refresh(mecanico)
        return mecanico

    def eliminar_mecanico(self, mecanico_id: int):
        mecanico = self.db.query(Mecanico).filter(Mecanico.mecanico_id == mecanico_id).first()
        if mecanico:
            self.db.delete(mecanico)
            self.db.commit()
        return mecanico
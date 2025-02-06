from sqlalchemy.orm import Session
from build.models.MecanicoModel import Mecanico
from build.service.ConexionQuito import get_db
from sqlalchemy import text




class MecanicoEntity:

    @staticmethod
    def crear_mecanico(mecanico_id: int,id_taller: int, especialidad: str, nombre_completo_mecanico: str):
        db = next(get_db())
        query = text("""
            INSERT INTO Mecanico (mecanico_id, id_taller, especialidad, nombre_completo_mecanico)
            VALUES (:mecanico_id, :id_taller, :especialidad, :nombre_completo_mecanico)
            """)
        db.execute(query, {
        'mecanico_id': mecanico_id,
        'id_taller': id_taller,
        'especialidad': especialidad,
        'nombre_completo_mecanico': nombre_completo_mecanico
    })
        db.commit()  # Asegúrate de hacer commit si estás realizando una operación que cambia datos.

    def obtener_mecanicos(self):
        return self.db.query(Mecanico).all()

    def actualizar_mecanico( mecanico_id: int = None, id_taller: int = None  ,especialidad: str = None, nombre_completo_mecanico: str = None):
        db = next(get_db())
        mecanico = db.query(Mecanico).filter(Mecanico.mecanico_id == mecanico_id).first()
        if mecanico:
            if especialidad is not None:
                mecanico.especialidad = especialidad
            if nombre_completo_mecanico is not None:
                mecanico.nombre_completo_mecanico = nombre_completo_mecanico
            if mecanico_id is not None:
                mecanico.mecanico_id = mecanico_id
            if id_taller is not None:
                mecanico.id_taller = id_taller
            db.commit()
            db.refresh(mecanico)
        return mecanico

    @staticmethod
    def eliminar_mecanico(mecanico_id: int):
        db = next(get_db())
        query = text("""
            SET XACT_ABORT ON;
            DELETE FROM Mecanico
            WHERE mecanico_id = :mecanico_id
        """)
        db.execute(query, {'mecanico_id': mecanico_id})
        db.commit()  # Aseguramos que el cambio sea persistido.

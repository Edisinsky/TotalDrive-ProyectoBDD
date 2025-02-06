from pymssql import IntegrityError

from build.models.MecanicoModel import Mecanico
from build.service.ConexionQuito import get_db
from build.service.ConexionCuenca import get_sb
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

    @staticmethod
    def obtener_mecanicos():
        db = next(get_db())
        return db.query(Mecanico).all()
    # Hacer el metodo estatico para no mandar como parametro el self
    @staticmethod
    def actualizar_mecanico(mecanico_id, id_taller: int = None, especialidad: str = None,
                            nombre_completo_mecanico: str = None):
        db = next(get_db())

        try:
            # Buscar el mecánico
            mecanico = db.query(Mecanico).filter(Mecanico.mecanico_id == mecanico_id).first()

            if not mecanico:
                return {"error": "Mecánico no encontrado"}

            # Actualizar solo los campos proporcionados
            if especialidad is not None:
                mecanico.especialidad = especialidad
            if nombre_completo_mecanico is not None:
                mecanico.nombre_completo_mecanico = nombre_completo_mecanico
            if id_taller is not None:
                # Verificar si el taller existe antes de asignarlo
                taller_existente = db.query(Taller).filter(Taller.id_taller == id_taller).first()
                if not taller_existente:
                    return {"error": "El taller especificado no existe"}
                mecanico.id_taller = id_taller

            db.commit()
            db.refresh(mecanico)
            return {"success": "Mecánico actualizado correctamente", "mecanico": mecanico}

        except IntegrityError as e:
            db.rollback()
            return {"error": f"No se pudo actualizar debido a restricciones: {str(e)}"}

        except Exception as e:
            db.rollback()
            return {"error": f"Error inesperado: {str(e)}"}

    @staticmethod
    def eliminar_mecanico(mecanico_id: int):
        db = next(get_db())

        try:
            # Iniciamos una transacción
            db.begin()

            # Primero eliminamos los registros relacionados en Servicio_Reservado
            query_servicio = text("""
                SET XACT_ABORT ON;
                DELETE FROM Servicio_Reservado
                WHERE mecanico_id = :mecanico_id
            """)
            db.execute(query_servicio, {'mecanico_id': mecanico_id})

            # Luego eliminamos el registro en Mecanico
            query_mecanico = text("""
                SET XACT_ABORT ON;
                DELETE FROM Mecanico
                WHERE mecanico_id = :mecanico_id
            """)
            db.execute(query_mecanico, {'mecanico_id': mecanico_id})

            # Confirmamos la transacción
            db.commit()

        except Exception as e:
            # Si algo sale mal, hacemos rollback de la transacción
            db.rollback()
            raise e
        finally:
            # Cerramos la conexión a la base de datos
            db.close()

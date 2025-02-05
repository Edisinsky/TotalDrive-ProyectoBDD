

class VehiculoEntity:
    def __init__(self, db: Session):
        self.db = db

    def crear_vehiculo(self, placa: str, id_propietario: int, modelo: str, marca: str):
        nuevo_vehiculo = Vehiculo(placa=placa, id_propietario=id_propietario, modelo=modelo, marca=marca)
        self.db.add(nuevo_vehiculo)
        self.db.commit()
        self.db.refresh(nuevo_vehiculo)
        return nuevo_vehiculo

    def obtener_vehiculos(self):
        return self.db.query(Vehiculo).all()

    def actualizar_vehiculo(self, placa: str, id_propietario: int = None, modelo: str = None, marca: str = None):
        vehiculo = self.db.query(Vehiculo).filter(Vehiculo.placa == placa).first()
        if vehiculo:
            if id_propietario is not None:
                vehiculo.id_propietario = id_propietario
            if modelo is not None:
                vehiculo.modelo = modelo
            if marca is not None:
                vehiculo.marca = marca
            self.db.commit()
            self.db.refresh(vehiculo)
        return vehiculo

    def eliminar_vehiculo(self, placa: str):
        vehiculo = self.db.query(Vehiculo).filter(Vehiculo.placa == placa).first()
        if vehiculo:
            self.db.delete(vehiculo)
            self.db.commit()
        return vehiculo

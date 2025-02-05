
# Crear una sesión para la base de datos
from build.service.MecanicoEntity import MecanicoEntity

# Crear una instancia del servicio Mecanico
mecanico = MecanicoEntity(db)

# Probar las operaciones CRUD
def main():
    # Crear un mecánico
    nuevo_mecanico = mecanico.crear_mecanico(1, "Electricidad", "Juan Pérez")
    print(f"Nuevo mecánico creado: {nuevo_mecanico.nombre_completo_mecanico}")

    # Obtener todos los mecánicos
    mecanicos = mecanico.obtener_mecanicos()
    print("Mecánicos en la base de datos:")
    for mecanico in mecanicos:
        print(f"- {mecanico.nombre_completo_mecanico} ({mecanico.especialidad})")

    # Actualizar un mecánico
    mecanico_actualizado = mecanico_service.actualizar_mecanico(nuevo_mecanico.mecanico_id, especialidad="Mecánica Automotriz")
    print(f"Mecánico actualizado: {mecanico_actualizado.nombre_completo_mecanico} con especialidad {mecanico_actualizado.especialidad}")

    # Eliminar un mecánico
    mecanico_service.eliminar_mecanico(nuevo_mecanico.mecanico_id)
    print(f"Mecánico con ID {nuevo_mecanico.mecanico_id} eliminado.")

if __name__ == "__main__":
    main()
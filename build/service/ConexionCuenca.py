from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

# Datos de conexión (ajusta los valores según tu configuración)
DB_DRIVER = "ODBC Driver 17 for SQL Server"

# # Conexión con el nodo de Quito
# DATABASE_QUITO = "nombre_base_quito"
# SERVER_QUITO = "IP_O_NOMBRE_SERVIDOR_QUITO"
# USERNAME = "tu_usuario"
# PASSWORD = "tu_contraseña"

# Conexión con el nodo de Cuenca
DATABASE_CUENCA = "TallerCuenca"
SERVER_CUENCA = "WIN-BPMN92IB7PH"
USERNAME_CUENCA = "Cuenca"
PASSWORD_CUENCA = "1234"

# Crear las URLs de conexión para SQLAlchemy
#DB_URL_QUITO = f"mssql+pyodbc://{USERNAME}:{PASSWORD}@{SERVER_QUITO}/{DATABASE_QUITO}?driver={DB_DRIVER}"
DB_URL_CUENCA = f"mssql+pyodbc://{USERNAME_CUENCA}:{PASSWORD_CUENCA}@{SERVER_CUENCA}/{DATABASE_CUENCA}?driver={DB_DRIVER}"

try:
        # Crear los motores de conexión
        #engine_quito = create_engine(DB_URL_QUITO)
        engine_cuenca = create_engine(DB_URL_CUENCA)

        # Crear las sesiones para interactuar con la base de datos
        #SessionQuito = sessionmaker(bind=engine_quito)
        SessionCuenca = sessionmaker(bind=engine_cuenca)
        #session_quito = SessionQuito()
        session_cuenca = SessionCuenca()

        result = session_cuenca.execute(text("SELECT * FROM Mecanico")).fetchall()
        print(result)
        print(f"✅ Conexión exitosa a {DATABASE_CUENCA} en {SERVER_CUENCA}")

except Exception as e:
        print(f"❌ Error al conectar con {DATABASE_CUENCA}: {e}")

finally:
        # Cerrar la sesión después de la verificación
        session_cuenca.close()



def get_sb():
    sb = SessionCuenca()  # Se crea una nueva sesión en cada solicitud
    try:
        yield sb
    finally:
        sb.close()  # Se cierra la sesión después de usarla
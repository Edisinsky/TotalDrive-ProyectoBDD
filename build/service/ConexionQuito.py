from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
# Datos de conexión (ajusta los valores según tu configuración)
DB_DRIVER = "ODBC Driver 17 for SQL Server"

# # Conexión con el nodo de Quito
DATABASE_QUITO = "TallerQuito"
SERVER_QUITO = "CHESCO"
USERNAME =  "quito"
PASSWORD = "1234"

# Conexión con el nodo de Cuenca
# DATABASE_CUENCA = "TallerCuenca"
# SERVER_CUENCA = ""
# USERNAME_CUENCA = ""
# PASSWORD_CUENCA = ""

# Crear las URLs de conexión para SQLAlchemy

DB_URL_QUITO = f"mssql+pyodbc://{USERNAME}:{PASSWORD}@{SERVER_QUITO}/{DATABASE_QUITO}?driver={DB_DRIVER}"


#DB_URL_CUENCA = f"mssql+pyodbc://{USERNAME_CUENCA}:{PASSWORD_CUENCA}@{SERVER_CUENCA}/{DATABASE_CUENCA}?driver={DB_DRIVER}"



try:
    # Crear los motores de conexión
    engine_quito = create_engine(DB_URL_QUITO)
    # engine_cuenca = create_engine(DB_URL_CUENCA)

    # Crear las sesiones para interactuar con la base de datos
    # SessionQuito = sessionmaker(bind=engine_quito)
    SessionQuito = sessionmaker(bind=engine_quito)
    # session_quito = SessionQuito()
    session_quito = SessionQuito()

    # Ejecutar una consulta de prueba
    result = session_quito.execute(text("SELECT * FROM Mecanico")).fetchall()
    print(result)
    print(f"✅ Conexión exitosa a {DATABASE_QUITO} en {SERVER_QUITO}")

except Exception as e:
    print(f"❌ Error al conectar con {DATABASE_QUITO}: {e}")

finally:
    # Cerrar la sesión después de la verificación
    session_quito.close()
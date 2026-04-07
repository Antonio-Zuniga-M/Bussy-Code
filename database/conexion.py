import mysql.connector

DB_HOST = "localhost"
DB_USER = "root"
DB_PASS = "123456789" # Recuerda a tu equipo ajustar esto en sus máquinas
DB_NAME = "BushiCode"

def obtener_conexion():
    """
    Establece y retorna la conexión a la base de datos.
    El esquema y las tablas deben ser creados previamente usando esquema.sql
    """
    try:
        conexion = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASS,
            database=DB_NAME
        )
        return conexion
    except mysql.connector.Error as e:
        print(f"Error de conexión a la base de datos: {e}")
        print("Asegúrate de haber ejecutado esquema.sql en tu gestor y tener las credenciales correctas.")
        return None

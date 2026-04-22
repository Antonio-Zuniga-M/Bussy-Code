import mysql.connector

DB_HOST = "localhost"
DB_PORT = 3310 # Debe cambiarse al local
DB_USER = "root" # Debe cambiarse al local
DB_PASS = "Palomo29MYSQL" # Debe cambiarse al local
DB_NAME = "BushiCode"

def obtener_conexion():
    """
    Establece y retorna la conexión a la base de datos.
    El esquema y las tablas deben ser creados previamente usando esquema.sql
    """
    try:
        conexion = mysql.connector.connect(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASS,
            database=DB_NAME
        )
        return conexion
    except mysql.connector.Error as e:
        print(f"Error de conexión a la base de datos: {e}")
        print("Asegúrate de haber ejecutado esquema.sql en tu gestor y tener las credenciales correctas.")
        return None

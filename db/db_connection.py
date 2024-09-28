import mysql.connector
from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()

# Configurar la conexión a la base de datos
def get_db_connection():
    connection = mysql.connector.connect(
        host=os.getenv('DB_HOST', 'localhost'),
        user=os.getenv('DB_USER', 'root'),
        password=os.getenv('DB_PASS', 'rodripaz'),
        database=os.getenv('DB_NAME', 'AutoWashDB')
    )
    return connection

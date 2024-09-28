from db.db_connection import get_db_connection

# Función para obtener todos los tipos de lavado
def get_all_tipo_lavado():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM TipoLavado")
    tipos_lavado = cursor.fetchall()
    conn.close()
    return tipos_lavado

# Función para obtener un tipo de lavado por su ID
def get_tipo_lavado_by_id(id_tipo_lavado):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM TipoLavado WHERE id_tipo_lavado = %s", (id_tipo_lavado,))
    tipo_lavado = cursor.fetchone()
    conn.close()
    return tipo_lavado

# Función para crear un nuevo tipo de lavado
def create_tipo_lavado(descripcion, costo_adicional):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO TipoLavado (descripcion, costo_adicional) VALUES (%s, %s)", 
                   (descripcion, costo_adicional))
    conn.commit()
    conn.close()

# Función para actualizar un tipo de lavado existente
def update_tipo_lavado(id_tipo_lavado, descripcion, costo_adicional):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE TipoLavado SET descripcion = %s, costo_adicional = %s WHERE id_tipo_lavado = %s", 
                   (descripcion, costo_adicional, id_tipo_lavado))
    conn.commit()
    conn.close()

# Función para eliminar un tipo de lavado
def delete_tipo_lavado(id_tipo_lavado):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM TipoLavado WHERE id_tipo_lavado = %s", (id_tipo_lavado,))
    conn.commit()
    conn.close()

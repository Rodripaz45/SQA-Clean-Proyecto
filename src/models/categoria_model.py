from db.db_connection import get_db_connection

# Función para obtener todas las categorías
def get_all_categories():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM CategoriasVehiculos")
    categories = cursor.fetchall()
    conn.close()
    return categories

# Función para obtener una categoría por su ID
def get_category_by_id(id_categoria):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM CategoriasVehiculos WHERE id_categoria = %s", (id_categoria,))
    category = cursor.fetchone()
    conn.close()
    return category

# Función para crear una nueva categoría
def create_category(tipo, precio_base):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO CategoriasVehiculos (tipo, precio_base) VALUES (%s, %s)", (tipo, precio_base))
    conn.commit()
    conn.close()

# Función para actualizar una categoría existente
def update_category(id_categoria, tipo, precio_base):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE CategoriasVehiculos SET tipo = %s, precio_base = %s WHERE id_categoria = %s", (tipo, precio_base, id_categoria))
    conn.commit()
    conn.close()

# Función para eliminar una categoría
def delete_category(id_categoria):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM CategoriasVehiculos WHERE id_categoria = %s", (id_categoria,))
    conn.commit()
    conn.close()

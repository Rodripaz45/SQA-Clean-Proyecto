from db.db_connection import get_db_connection

# Función para obtener todas las reservas
def get_all_reservas():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)  # Usar dictionary=True para resultados en formato de diccionario
    cursor.execute("SELECT * FROM Reservas")
    reservas = cursor.fetchall()
    conn.close()
    return reservas

# Función para obtener una reserva por su ID
def get_reserva_by_id(id_reserva):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Reservas WHERE id_reserva = %s", (id_reserva,))
    reserva = cursor.fetchone()
    conn.close()
    return reserva

# Función para crear una nueva reserva
def create_reserva(nombre_cliente, celular_cliente, id_categoria, id_tipo_lavado, fecha_hora_reserva, estado_reserva, lavado_motor):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    # Obtener el precio base de la categoría
    cursor.execute("SELECT precio_base FROM CategoriasVehiculos WHERE id_categoria = %s", (id_categoria,))
    categoria = cursor.fetchone()

    # Obtener el costo adicional del tipo de lavado
    cursor.execute("SELECT costo_adicional FROM TipoLavado WHERE id_tipo_lavado = %s", (id_tipo_lavado,))
    tipo_lavado = cursor.fetchone()

    # Calcular el precio total
    precio_base = categoria['precio_base'] if categoria else 0
    costo_adicional = tipo_lavado['costo_adicional'] if tipo_lavado else 0
    precio_total = precio_base + costo_adicional + (10 if lavado_motor else 0)

    # Crear la reserva
    cursor.execute("INSERT INTO Reservas (nombre_cliente, celular_cliente, id_categoria, id_tipo_lavado, fecha_hora_reserva, estado_reserva, precio_total, lavado_motor) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", 
                   (nombre_cliente, celular_cliente, id_categoria, id_tipo_lavado, fecha_hora_reserva, estado_reserva, precio_total, lavado_motor))
    conn.commit()
    conn.close()

# Función para actualizar una reserva existente
def update_reserva(id_reserva, nombre_cliente, celular_cliente, id_categoria, id_tipo_lavado, fecha_hora_reserva, estado_reserva, lavado_motor):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    # Obtener el precio base de la categoría
    cursor.execute("SELECT precio_base FROM CategoriasVehiculos WHERE id_categoria = %s", (id_categoria,))
    categoria = cursor.fetchone()

    # Obtener el costo adicional del tipo de lavado
    cursor.execute("SELECT costo_adicional FROM TipoLavado WHERE id_tipo_lavado = %s", (id_tipo_lavado,))
    tipo_lavado = cursor.fetchone()

    # Calcular el precio total
    precio_base = categoria['precio_base'] if categoria else 0
    costo_adicional = tipo_lavado['costo_adicional'] if tipo_lavado else 0
    precio_total = precio_base + costo_adicional + (10 if lavado_motor else 0)

    # Actualizar la reserva
    cursor.execute("UPDATE Reservas SET nombre_cliente = %s, celular_cliente = %s, id_categoria = %s, id_tipo_lavado = %s, fecha_hora_reserva = %s, estado_reserva = %s, precio_total = %s, lavado_motor = %s WHERE id_reserva = %s", 
                   (nombre_cliente, celular_cliente, id_categoria, id_tipo_lavado, fecha_hora_reserva, estado_reserva, precio_total, lavado_motor, id_reserva))
    conn.commit()
    conn.close()

# Función para eliminar una reserva
def delete_reserva(id_reserva):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Reservas WHERE id_reserva = %s", (id_reserva,))
    conn.commit()
    conn.close()

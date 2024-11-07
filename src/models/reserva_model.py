from db.db_connection import get_db_connection

# Función para obtener todas las reservas
def get_all_reservas():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)  # Usar dictionary=True para resultados en formato de diccionario
    cursor.execute("SELECT r.id_reserva, r.nombre_cliente, r.celular_cliente, r.fecha_hora_reserva, r.estado_reserva, r.precio_total, r.lavado_motor, c.tipo AS tipo_categoria, t.descripcion AS descripcion_tipo_lavado FROM Reservas r JOIN      CategoriasVehiculos c ON r.id_categoria = c.id_categoria JOIN TipoLavado t ON r.id_tipo_lavado = t.id_tipo_lavado; ")
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

# src/models/reserva_model.py
def update_reserva(id_reserva, estado_reserva):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    # Obtener el número de teléfono antes de actualizar el estado
    cursor.execute("SELECT celular_cliente FROM Reservas WHERE id_reserva = %s", (id_reserva,))
    result = cursor.fetchone()
    if not result:
        cursor.close()
        conn.close()
        return None  # Retorna None si la reserva no existe

    celular_cliente = result['celular_cliente']

    # Actualizar el estado de la reserva
    cursor.execute("UPDATE Reservas SET estado_reserva = %s WHERE id_reserva = %s", 
                   (estado_reserva, id_reserva))
    conn.commit()

    cursor.close()
    conn.close()

    # Retornar el número de teléfono del cliente
    return celular_cliente

# Función para eliminar una reserva
def delete_reserva(id_reserva):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Reservas WHERE id_reserva = %s", (id_reserva,))
    conn.commit()
    conn.close()

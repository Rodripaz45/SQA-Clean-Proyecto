from flask import jsonify, request
from src.models.reserva_model import get_all_reservas, get_reserva_by_id, create_reserva, update_reserva, delete_reserva

# Obtener todas las reservas
def list_reservas():
    reservas = get_all_reservas()
    
    # Convertir los resultados a un formato serializable
    for reserva in reservas:
        reserva['fecha_hora_reserva'] = reserva['fecha_hora_reserva'].strftime("%Y-%m-%d %H:%M:%S")  # Convertir a string

    return jsonify(reservas), 200

# Obtener una reserva por su ID
def get_reserva(id_reserva):
    reserva = get_reserva_by_id(id_reserva)
    if reserva:
        reserva['fecha_hora_reserva'] = reserva['fecha_hora_reserva'].strftime("%Y-%m-%d %H:%M:%S")  # Convertir a string
        return jsonify(reserva), 200
    else:
        return jsonify({"error": "Reserva no encontrada"}), 404

# Crear una nueva reserva
def add_reserva():
    data = request.get_json()
    nombre_cliente = data.get('nombre_cliente')
    celular_cliente = data.get('celular_cliente')
    id_categoria = data.get('id_categoria')
    id_tipo_lavado = data.get('id_tipo_lavado')
    fecha_hora_reserva = data.get('fecha_hora_reserva')  # Debe ser un string en formato adecuado
    estado_reserva = data.get('estado_reserva')
    lavado_motor = data.get('lavado_motor', False)

    create_reserva(nombre_cliente, celular_cliente, id_categoria, id_tipo_lavado, fecha_hora_reserva, estado_reserva, lavado_motor)
    return jsonify({"message": "Reserva creada correctamente"}), 201

# Actualizar una reserva existente
def edit_reserva(id_reserva):
    data = request.get_json()
    nombre_cliente = data.get('nombre_cliente')
    celular_cliente = data.get('celular_cliente')
    id_categoria = data.get('id_categoria')
    id_tipo_lavado = data.get('id_tipo_lavado')
    fecha_hora_reserva = data.get('fecha_hora_reserva')  # Debe ser un string en formato adecuado
    estado_reserva = data.get('estado_reserva')
    lavado_motor = data.get('lavado_motor', False)

    update_reserva(id_reserva, nombre_cliente, celular_cliente, id_categoria, id_tipo_lavado, fecha_hora_reserva, estado_reserva, lavado_motor)
    return jsonify({"message": "Reserva actualizada correctamente"}), 200

# Eliminar una reserva
def remove_reserva(id_reserva):
    delete_reserva(id_reserva)
    return jsonify({"message": "Reserva eliminada correctamente"}), 200

from flask import jsonify, request
from src.models.tipo_lavado_model import get_all_tipo_lavado, get_tipo_lavado_by_id, create_tipo_lavado, update_tipo_lavado, delete_tipo_lavado

# Obtener todos los tipos de lavado
def list_tipo_lavado():
    tipos_lavado = get_all_tipo_lavado()
    return jsonify(tipos_lavado), 200

# Obtener un tipo de lavado por su ID
def get_tipo_lavado(id_tipo_lavado):
    tipo_lavado = get_tipo_lavado_by_id(id_tipo_lavado)
    if tipo_lavado:
        return jsonify(tipo_lavado), 200
    else:
        return jsonify({"error": "Tipo de lavado no encontrado"}), 404

# Crear un nuevo tipo de lavado
def add_tipo_lavado():
    data = request.get_json()
    descripcion = data.get('descripcion')
    costo_adicional = data.get('costo_adicional')
    create_tipo_lavado(descripcion, costo_adicional)
    return jsonify({"message": "Tipo de lavado creado correctamente"}), 201

# Actualizar un tipo de lavado existente
def edit_tipo_lavado(id_tipo_lavado):
    data = request.get_json()
    descripcion = data.get('descripcion')
    costo_adicional = data.get('costo_adicional')
    update_tipo_lavado(id_tipo_lavado, descripcion, costo_adicional)
    return jsonify({"message": "Tipo de lavado actualizado correctamente"}), 200

# Eliminar un tipo de lavado
def remove_tipo_lavado(id_tipo_lavado):
    delete_tipo_lavado(id_tipo_lavado)
    return jsonify({"message": "Tipo de lavado eliminado correctamente"}), 200

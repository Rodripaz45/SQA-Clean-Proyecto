from flask import jsonify, request
from src.models.categoria_model import get_all_categories, get_category_by_id, create_category, update_category, delete_category

# Obtener todas las categorías
def list_categories():
    categories = get_all_categories()
    return jsonify(categories), 200

# Obtener una categoría por su ID
def get_category(id_categoria):
    category = get_category_by_id(id_categoria)
    if category:
        return jsonify(category), 200
    else:
        return jsonify({"error": "Categoría no encontrada"}), 404

# Crear una nueva categoría
def add_category():
    data = request.get_json()
    tipo = data.get('tipo')
    precio_base = data.get('precio_base')
    create_category(tipo, precio_base)
    return jsonify({"message": "Categoría creada correctamente"}), 201

# Actualizar una categoría existente
def edit_category(id_categoria):
    data = request.get_json()
    tipo = data.get('tipo')
    precio_base = data.get('precio_base')
    update_category(id_categoria, tipo, precio_base)
    return jsonify({"message": "Categoría actualizada correctamente"}), 200

# Eliminar una categoría
def remove_category(id_categoria):
    delete_category(id_categoria)
    return jsonify({"message": "Categoría eliminada correctamente"}), 200

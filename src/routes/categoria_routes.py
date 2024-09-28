from flask import Blueprint
from src.controllers.categoria_controller import list_categories, get_category, add_category, edit_category, remove_category

# Crear un blueprint para las rutas de categoría
categoria_bp = Blueprint('categoria', __name__)

# Definir las rutas CRUD
categoria_bp.route('/categorias', methods=['GET'])(list_categories)
categoria_bp.route('/categorias/<int:id_categoria>', methods=['GET'])(get_category)
categoria_bp.route('/categorias', methods=['POST'])(add_category)
categoria_bp.route('/categorias/<int:id_categoria>', methods=['PUT'])(edit_category)
categoria_bp.route('/categorias/<int:id_categoria>', methods=['DELETE'])(remove_category)

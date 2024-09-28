from flask import Blueprint
from src.controllers.tipo_lavado_controller import list_tipo_lavado, get_tipo_lavado, add_tipo_lavado, edit_tipo_lavado, remove_tipo_lavado

# Crear un blueprint para las rutas de tipo de lavado
tipo_lavado_bp = Blueprint('tipo_lavado', __name__)

# Definir las rutas CRUD
tipo_lavado_bp.route('/tipolavado', methods=['GET'])(list_tipo_lavado)
tipo_lavado_bp.route('/tipolavado/<int:id_tipo_lavado>', methods=['GET'])(get_tipo_lavado)
tipo_lavado_bp.route('/tipolavado', methods=['POST'])(add_tipo_lavado)
tipo_lavado_bp.route('/tipolavado/<int:id_tipo_lavado>', methods=['PUT'])(edit_tipo_lavado)
tipo_lavado_bp.route('/tipolavado/<int:id_tipo_lavado>', methods=['DELETE'])(remove_tipo_lavado)

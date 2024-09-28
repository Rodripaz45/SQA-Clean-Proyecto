from flask import Blueprint
from src.controllers.reserva_controller import list_reservas, get_reserva, add_reserva, edit_reserva, remove_reserva

# Crear un blueprint para las rutas de reserva
reserva_bp = Blueprint('reserva', __name__)

# Definir las rutas CRUD
reserva_bp.route('/reservas', methods=['GET'])(list_reservas)
reserva_bp.route('/reservas/<int:id_reserva>', methods=['GET'])(get_reserva)
reserva_bp.route('/reservas', methods=['POST'])(add_reserva)
reserva_bp.route('/reservas/<int:id_reserva>', methods=['PUT'])(edit_reserva)
reserva_bp.route('/reservas/<int:id_reserva>', methods=['DELETE'])(remove_reserva)

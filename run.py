from flask import Flask
from dotenv import load_dotenv
from src.routes.categoria_routes import categoria_bp
from src.routes.tipo_lavado_routes import tipo_lavado_bp
from src.routes.reserva_routes import reserva_bp

import os

# Cargar las variables del archivo .env
load_dotenv()

# Crear la aplicación Flask
app = Flask(__name__)

app.register_blueprint(categoria_bp)
app.register_blueprint(tipo_lavado_bp)  
app.register_blueprint(reserva_bp)

# Ejecutar la aplicación en el puerto especificado
if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))  # Utiliza el puerto especificado en .env o el puerto 5000 por defecto
    app.run(host="0.0.0.0", port=port)

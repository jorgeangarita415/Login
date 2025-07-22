from flask import Flask
from models import db
from auth_routes import auth_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar la base de datos
db.init_app(app)

# Registrar el blueprint de autenticación
app.register_blueprint(auth_bp)

# Crear las tablas antes de la primera petición
@app.before_request
def create_tables():
    db.create_all()

# Ejecutar el servidor
if __name__ == '__main__':
    app.run(debug=True)

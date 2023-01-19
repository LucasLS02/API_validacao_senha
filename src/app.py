from flask import Flask
from flask_cors import CORS

from src.controllers.password_controller import password_controller as password_controller_blueprint


app = Flask(__name__)

app.register_blueprint(password_controller_blueprint)

CORS(app)

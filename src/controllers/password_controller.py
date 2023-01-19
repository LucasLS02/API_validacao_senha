from flask import Blueprint


password_controller = Blueprint('password_controller', __name__)


@password_controller.route('/verify', methods=['POST'])
def verify():
    return {'data': 'Hello World!'}, 200

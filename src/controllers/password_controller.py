from flask import Blueprint, request

from marshmallow.exceptions import ValidationError

from src.schemas.password_schema import PasswordSchema


password_controller = Blueprint('password_controller', __name__)


@password_controller.route('/verify', methods=['POST'])
def verify():
    try:

        data = PasswordSchema().load(request.json)

    except ValidationError as e:
        return {'errors': e.messages}
    except Exception as e:
        print(e)

    return {'data': data}, 200

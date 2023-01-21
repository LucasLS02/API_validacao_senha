from flask import Blueprint, request

from marshmallow.exceptions import ValidationError

from src.schemas.password_schema import PasswordSchema, PasswordVerificationResponseSchema

password_controller = Blueprint('password_controller', __name__)


@password_controller.route('/verify', methods=['POST'])
def verify():
    try:
        data = PasswordSchema().load(request.json)

        response = {
            'verify': True,
            'noMatch': []
        }

        for rule in data['rules']:
            match rule['rule']:
                case 'minSize':
                    if len(data['password']) > rule['value']:
                        response['noMatch'].append('minSize')
                        response['verify'] = False

                case 'minUppercase':
                    response['verify'] = False

                case 'minLowercase':
                    response['verify'] = False

                case 'minDigit':
                    response['verify'] = False

                case 'minSpecialChars':
                    response['verify'] = False

                case 'noRepeted':
                    response['verify'] = False

        response = PasswordVerificationResponseSchema().dump(response)

    except ValidationError as e:
        return {'error': e.messages}, 422
    except Exception as e:
        print(e)
        return {'error': 'Internal Server Error'}, 500

    return {'data': response}, 200

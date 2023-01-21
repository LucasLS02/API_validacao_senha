from flask import Blueprint, request

from marshmallow.exceptions import ValidationError

from src.schemas.password_schema import PasswordSchema, PasswordVerificationResponseSchema


password_controller = Blueprint('password_controller', __name__)


@password_controller.route('/verify', methods=['POST'])
def verify_password():
    try:
        data = PasswordSchema().load(request.json)

        response = {
            'verify': True,
            'noMatch': []
        }

        password = data['password'].strip()

        for rule in data['rules']:
            match rule['rule']:
                case 'minSize':
                    if len(password) < rule['value']:
                        response['noMatch'].append('minSize')
                        response['verify'] = False

                case 'minUppercase':
                    count = 0

                    for char in password:
                        if char.isupper():
                            count += 1

                    if count < rule['value']:
                        response['noMatch'].append('minUppercase')
                        response['verify'] = False

                case 'minLowercase':
                    count = 0

                    for char in password:
                        if char.islower():
                            count += 1

                    if count < rule['value']:
                        response['noMatch'].append('minLowercase')
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

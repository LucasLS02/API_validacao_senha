import re

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
                    if re.search('[A-Z]+', password):
                        count = 0

                        for char in password:
                            if char.isupper():
                                count += 1

                        if count < rule['value']:
                            response['noMatch'].append('minUppercase')
                            response['verify'] = False

                    else:
                        response['noMatch'].append('minUppercase')
                        response['verify'] = False

                case 'minLowercase':
                    if re.search('[a-z]+', password):
                        count = 0

                        for char in password:
                            if char.islower():
                                count += 1

                        if count < rule['value']:
                            response['noMatch'].append('minLowercase')
                            response['verify'] = False


                    else:
                        response['noMatch'].append('minLowercase')
                        response['verify'] = False

                case 'minDigit':
                    if re.search('\d', password):
                        count = 0

                        for char in password:
                            if char.isdigit():
                                count += 1

                        if count < rule['value']:
                            response['noMatch'].append('minDigit')
                            response['verify'] = False
                    else:
                        response['noMatch'].append('minDigit')
                        response['verify'] = False

                case 'minSpecialChars':
                    special_characters = re.findall("[!@#$%&*()_+=|<>?{}\\[\\]~-]", password)

                    if len(special_characters) < rule['value']:
                        response['noMatch'].append('minSpecialChars')
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

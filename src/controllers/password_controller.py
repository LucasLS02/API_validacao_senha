import re

from flask import Blueprint, request

from marshmallow.exceptions import ValidationError

from src.schemas.password_schema import PasswordSchema, PasswordVerificationResponseSchema


password_controller = Blueprint('password_controller', __name__)


"""
It receives a password and a list of rules, and returns a list of rules that the password does not match
:return: A dictionary with the key 'data' and the value of the response variable.
"""


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
                    if re.search('[A-Z]+', password) or rule['value'] == 0:
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
                    if re.search('[a-z]+', password) or rule['value'] == 0:
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
                    if re.search('\d', password) or rule['value'] == 0:
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
                    count = 0

                    for char in range(0, len(password) - 1):
                        if password[char] == password[char + 1]:
                            count += 1

                    if count > 0:
                        response['noMatch'].append('noRepeted')
                        response['verify'] = False

        response = PasswordVerificationResponseSchema().dump(response)

    except ValidationError as e:
        return {'error': e.messages}, 422
    except Exception as e:
        print(e)
        return {'error': 'Internal Server Error'}, 500

    return {'data': response}, 200

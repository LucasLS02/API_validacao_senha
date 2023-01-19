from marshmallow import Schema, fields, validate


class PasswordRulesSchema(Schema):
    rule = fields.String(required=False, allow_none=False, validate=validate.OneOf(['minSize', 'minUppercase',
                                                                                   'minLowercase', 'minDigit',
                                                                                   'minSpecialChars', 'noRepeted']))
    value = fields.Int(required=False, allow_none=False, validate=validate.Range(min=0))

    class Meta:
        fields = ('rule', 'value')
        ordered = True


class PasswordSchema(Schema):
    password = fields.String(required=True, allow_none=False)
    rules = fields.List(fields.Nested(PasswordRulesSchema), required=True, allow_none=False)

    class Meta:
        fields = ('password', 'rules')
        ordered = True

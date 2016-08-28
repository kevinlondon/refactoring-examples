class User:

    _fields = [
        'email',
        'first_name',
        'last_name'
    ]

    def __init__(self, data):
        self.data = data

    def validate(self):
        for field in self._fields:
            method_name = 'validate_{}'.format(field)
            validate_field = getattr(self, method_name)
            validate_field()

    def validate_email(self):
        if '@' not in self.data['email']:
            raise ValueError('Invalid email provided.')

    def validate_first_name(self):
        if len(self.data['first_name']) > 50:
            raise ValueError('First name too long.')

    def validate_last_name(self):
        if len(self.data['last_name']) > 100:
            raise ValueError('Last name too long.')

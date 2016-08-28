class User:

    def __init__(self, data):
        self.data = data

    def validate(self):
        self.validate_email()
        self.validate_first_name()
        self.validate_last_name()

    def validate_email(self):
        if '@' not in self.data['email']:
            raise ValueError('Invalid email provided.')

    def validate_first_name(self):
        if len(self.data['first_name']) > 50:
            raise ValueError('First name too long.')

    def validate_last_name(self):
        if len(self.data['last_name']) > 100:
            raise ValueError('Last name too long.')

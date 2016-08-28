class User:

    def __init__(self, data):
        self.data = data

    def create(self):
        self.validate()
        self.save()

    def validate(self):
        if '@' not in self.data['email']:
            raise ValueError('Invalid email provided.')

        if len(self.data['first_name']) > 50:
            raise ValueError('First name too long.')

        if len(self.data['last_name']) > 100:
            raise ValueError('Last name too long.')

    def save(self):
        # Persist into db
        pass

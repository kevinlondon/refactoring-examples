import pytest
from toothpaste4 import User

def assert_raises_error(data, expected_message):
    user = User(data=data)
    with pytest.raises(ValueError) as excinfo:
        user.validate()

    assert expected_message in str(excinfo.value)


class TestValidateUser:
    def test_invalid_email_raises_error(self):
        data = {
            'first_name': 'foo',
            'email': 'bademail',
            'last_name': 'lee',
        }
        assert_raises_error(data, 'Invalid email provided')

    def test_long_first_name_raises_error(self):
        data = {
            'first_name': 'f' * 1000,
            'last_name': 'baz',
            'email': 'bar@baz.com',
        }
        assert_raises_error(data, 'First name too long')

    def test_long_last_name_raises_error(self):
        data = {
            'first_name': 'foo',
            'last_name': 'l' * 1000,
            'email': 'bar@baz.com',
        }
        assert_raises_error(data, 'Last name too long')

    def test_invalid_phone_number_raises_error(self):
        data = {'phone_number': 'no_phone'}
        user = User(data)
        with pytest.raises(ValueError):
            user.validate_phone_number()

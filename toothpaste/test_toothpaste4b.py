
import pytest
from toothpaste4 import User

def assert_raises_error(data, expected_message, field):
    user = User(data=data)
    user._fields = [field]
    with pytest.raises(ValueError) as excinfo:
        user.validate()

    assert expected_message in str(excinfo.value)


class TestValidateUser:
    def test_invalid_email_raises_error(self):
        data = {'email': 'bademail'}
        assert_raises_error(
            data, 'Invalid email provided',
            field='email'
        )

    def test_long_first_name_raises_error(self):
        data = {'first_name': 'f' * 1000}
        assert_raises_error(
            data, 'First name too long',
            field='first_name'
        )

    def test_long_last_name_raises_error(self):
        data = {'last_name': 'l' * 1000}
        assert_raises_error(
            data, 'Last name too long',
            field='last_name'
        )

    def test_invalid_phone_number_raises_error(self):
        data = {'phone_number': 'notaphone'}
        assert_raises_error(
            data, 'Phone number',
            field='phone_number'
        )

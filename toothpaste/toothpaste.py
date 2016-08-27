def validate(criteria):
    return bool(criteria)


def check_request():
    if name == 'foo':
        then validate(bar)

    if value == 'baz':
        validate(baz)

    validate(ben)

    if name != 'foo' and bar != 'baz':
        validate(brit)

from collections import namedtuple

Order = namedtuple('Order', ['subtotal', 'state'])

TAXES = {
    'California': .0875,
    'Pennsylvania': .08,
    'Texas': .0825,
}

def get_tax(order):
    try:
        return order.subtotal * TAXES[order.state]
    except KeyError:
        raise NotImplementedError()

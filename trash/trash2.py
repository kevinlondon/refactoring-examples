from collections import namedtuple

Order = namedtuple('Order', ['subtotal', 'state'])

def get_tax(order):
    if order.state == 'California':
        return order.subtotal * .0875
    elif order.state == 'Pennsylvania':
        return order.subtotal * .08
    elif order.state == 'Texas':
        return order.subtotal * .0825
    else:
        raise NotImplementedError()

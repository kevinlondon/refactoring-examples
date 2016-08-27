import pytest
from trash1 import get_tax, Order

def tax_equals_percent(state, percent):
    subtotal = 10
    order = Order(subtotal=subtotal, state=state)
    return get_tax(order) == subtotal * percent

def test_get_tax_for_california():
    assert tax_equals_percent(state='California', percent=.0875)

def test_get_tax_for_pennsylvania():
    assert tax_equals_percent(state='Pennsylvania', percent=.08)

def test_get_tax_for_texas():
    assert tax_equals_percent(state='Texas', percent=.0825)

def test_it_raises_not_implemented_error_for_others():
    with pytest.raises(NotImplementedError):
        tax_equals_percent(state='Equador', percent=0)

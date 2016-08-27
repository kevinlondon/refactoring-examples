import pytest
from trash1 import get_tax, Order

def test_get_tax_for_ca():
    order = Order(subtotal=10, state='California')
    assert get_tax(order) == 10 * .0875

def test_get_tax_for_pa():
    order = Order(subtotal=10, state='Pennsylvania')
    assert get_tax(order) == 10 * 0.08

def test_it_raises_not_implemented_error_for_others():
    with pytest.raises(NotImplementedError):
        order = Order(subtotal=10, state='Equador')
        assert get_tax(order) == 0

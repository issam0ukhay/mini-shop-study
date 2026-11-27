from decimal import Decimal

import pytest

from shop import Cart, Product
from shop.discounts import InvalidDiscountCode

MUG = Product("MUG-01", "Mug", Decimal("12.50"))
NOTEBOOK = Product("NB-01", "Notebook", Decimal("4.99"))


def make_cart() -> Cart:
    cart = Cart()
    cart.add(MUG, 2)
    cart.add(NOTEBOOK)
    return cart


def test_adding_same_product_increments_quantity():
    cart = Cart()
    cart.add(MUG)
    cart.add(MUG, 2)
    assert [(i.product.sku, i.quantity) for i in cart.items] == [("MUG-01", 3)]


def test_add_rejects_non_positive_quantity():
    with pytest.raises(ValueError):
        Cart().add(MUG, 0)


def test_subtotal():
    assert make_cart().subtotal() == Decimal("29.99")


def test_total_without_discount():
    cart = make_cart()
    assert cart.tax() == Decimal("6.00")
    assert cart.total() == Decimal("35.99")


def test_total_with_discount():
    cart = make_cart()
    cart.apply_discount("welcome10")
    assert cart.discount() == Decimal("3.00")
    assert cart.tax() == Decimal("5.40")
    assert cart.total() == Decimal("32.39")


def test_invalid_discount_code():
    with pytest.raises(InvalidDiscountCode):
        make_cart().apply_discount("NOPE")


def test_update_quantity():
    cart = make_cart()
    cart.update_quantity("MUG-01", 5)
    assert cart.subtotal() == Decimal("67.49")

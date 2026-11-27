from decimal import ROUND_HALF_UP, Decimal

from shop.discounts import discount_rate
from shop.models import CartItem, Product
from shop.tax import TaxCalculator

CENT = Decimal("0.01")


def _to_cents(amount: Decimal) -> Decimal:
    return amount.quantize(CENT, rounding=ROUND_HALF_UP)


class Cart:
    def __init__(self, tax_calculator: TaxCalculator | None = None) -> None:
        self._items: dict[str, CartItem] = {}
        self._discount_rate = Decimal("0")
        self._tax = tax_calculator or TaxCalculator()

    @property
    def items(self) -> list[CartItem]:
        return list(self._items.values())

    def add(self, product: Product, quantity: int = 1) -> None:
        if quantity <= 0:
            raise ValueError("quantity must be positive")
        if product.sku in self._items:
            self._items[product.sku].quantity += quantity
        else:
            self._items[product.sku] = CartItem(product, quantity)

    def remove(self, sku: str) -> None:
        del self._items[sku]

    def update_quantity(self, sku: str, quantity: int) -> None:
        self._items[sku].quantity = quantity

    def apply_discount(self, code: str) -> None:
        self._discount_rate = discount_rate(code)

    def subtotal(self) -> Decimal:
        return sum((item.line_total for item in self._items.values()), Decimal("0"))

    def discount(self) -> Decimal:
        return _to_cents(self.subtotal() * self._discount_rate)

    def tax(self) -> Decimal:
        return self._tax.tax_for(self.subtotal())

    def total(self) -> Decimal:
        return self.subtotal() - self.discount() + self.tax()

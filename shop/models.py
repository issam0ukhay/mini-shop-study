from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class Product:
    sku: str
    name: str
    price: Decimal


@dataclass
class CartItem:
    product: Product
    quantity: int

    @property
    def line_total(self) -> Decimal:
        return self.product.price * self.quantity

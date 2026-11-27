# mini-shop

A tiny shopping-cart library: products, a cart, discount codes and tax.

## Usage

```python
from decimal import Decimal
from shop import Cart, Product

cart = Cart()
cart.add(Product("MUG-01", "Mug", Decimal("12.50")), quantity=2)
cart.add(Product("NB-01", "Notebook", Decimal("4.99")))
cart.apply_discount("WELCOME10")   # codes are case-insensitive

cart.subtotal()   # Decimal('29.99')
cart.discount()   # Decimal('3.00')
cart.tax()        # Decimal('5.40')  -> 20 % of the discounted amount
cart.total()      # Decimal('32.39')
```

Adding a product that is already in the cart increases its quantity.
An unknown discount code raises `shop.discounts.InvalidDiscountCode`.

### Discount codes

| Code        | Discount |
|-------------|----------|
| `WELCOME10` | 10 %     |
| `VIP20`     | 20 %     |

Amounts are `Decimal` values rounded to the cent (half up).

## Development

```bash
pip install -e ".[test]"
pytest
```

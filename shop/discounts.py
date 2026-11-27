from decimal import Decimal

DISCOUNT_CODES = {
    "WELCOME10": Decimal("0.10"),
    "VIP20": Decimal("0.20"),
}


class InvalidDiscountCode(ValueError):
    """Raised when a discount code does not exist."""


def discount_rate(code: str) -> Decimal:
    """Return the discount rate (0.10 = 10 %) for a code, case-insensitive."""
    try:
        return DISCOUNT_CODES[code.strip().upper()]
    except KeyError:
        raise InvalidDiscountCode(code) from None

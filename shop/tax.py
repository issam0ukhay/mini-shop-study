from decimal import Decimal


class TaxCalculator:
    """Computes the tax for an amount at a fixed rate."""

    def __init__(self, rate: Decimal = Decimal("0.20")) -> None:
        self.rate = rate

    def tax_for(self, amount: Decimal) -> Decimal:
        return round(amount * self.rate, 2)

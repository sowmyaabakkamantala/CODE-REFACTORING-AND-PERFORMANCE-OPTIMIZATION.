from __future__ import annotations

class Pizza:
    """Represents a pizza with size and list of toppings."""

    def __init__(self, size: str) -> None:
        """
        Args:
            size: one of 'small', 'medium', 'large'
        """
        self.size = size
        self.toppings: list[str] = []

    def add_topping(self, topping: str) -> None:
        """Add a topping to this pizza."""
        self.toppings.append(topping)

    def get_price(self) -> float:
        """Compute the price: base + size adjustment + toppings."""
        base = 10.0
        if self.size == 'large':
            base += 5.0
        return base + 2.0 * len(self.toppings)

    def __str__(self) -> str:
        """Return a readable description of the pizza."""
        if self.toppings:
            tops = ", ".join(self.toppings)
            return f"{self.size} pizza with {tops}"
        return f"{self.size} plain pizza"


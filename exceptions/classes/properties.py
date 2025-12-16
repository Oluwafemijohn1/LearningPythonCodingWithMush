class Product:
    def __init__(self, name: str, price: float):
        self.__price = price
        self.name = name

    @property
    def price(self) -> float:
        """Get the price of the product."""
        return self.__price

    """A class representing a product with a name and price."""
    @price.setter
    def price(self, value: float):
        """Set the price of the product, ensuring it is non-negative."""
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self.__price = value


product = Product("Laptop", 1000.0)
product.price = 1200.0  # Using the property setter
print(f"Product price: {product.price}")  # Using the property getter
try:
    product.price = -500.0  # This will raise a ValueError
except ValueError as e:
    print(f"Error: {e}")

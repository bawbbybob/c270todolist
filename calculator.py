"""Calculator logic module."""


class Calculator:
    """Basic arithmetic operations."""

    def add(self, a, b):
        """Adds two numbers."""
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Both arguments must be numbers")
        return a + b

    def subtract(self, a, b):
        """Subtracts the second number from the first."""
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Both arguments must be numbers")
        return a - b

    def multiply(self, a, b):
        """Multiplies both numbers."""
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Both arguments must be numbers")
        return a * b

    def divide(self, a, b):
        """Divides the first number by the second. Returns error if dividing by 0."""
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Both arguments must be numbers")
        if b == 0:
            return "Error: Division by zero is not allowed."
        return a / b


# Example usage
calc = Calculator()

# Addition
result_add = calc.add(10, 5)
print(f"10 + 5 = {result_add}")

# Subtraction
result_sub = calc.subtract(10, 5)
print(f"10 - 5 = {result_sub}")

# Multiplication
result_mul = calc.multiply(10, 5)
print(f"10 * 5 = {result_mul}")

# Division
result_div = calc.divide(10, 5)
print(f"10 / 5 = {result_div}")

# Division by zero
result_div_zero = calc.divide(10, 0)
print(f"10 / 0 = {result_div_zero}")
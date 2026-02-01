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
RESULT_ADD = calc.add(10, 5)
print(f"10 + 5 = {RESULT_ADD}")

# Subtraction
RESULT_SUB = calc.subtract(10, 5)
print(f"10 - 5 = {RESULT_SUB}")

# Multiplication
RESULT_MUL = calc.multiply(10, 5)
print(f"10 * 5 = {RESULT_MUL}")

# Division
RESULT_DIV = calc.divide(10, 5)
print(f"10 / 5 = {RESULT_DIV}")

# Division by zero
RESULT_DIV_ZERO = calc.divide(10, 0)
print(f"10 / 0 = {RESULT_DIV_ZERO}")

"""Flask web app for the calculator UI."""

from flask import Flask, render_template, request
from calculator import Calculator

app = Flask(__name__)
calc = Calculator()

@app.route('/', methods=['GET', 'POST'])
def index():
    """Render calculator page and process operations."""
    result = ""

    if request.method == 'POST':
        number1 = float(request.form.get('num1'))
        number2 = float(request.form.get('num2'))
        operation = request.form.get('operation')

        if operation == 'add':
            result = calc.add(number1, number2)

        elif operation == 'subtract':
            result = calc.subtract(number1, number2)

        elif operation == 'multiply':
            result = calc.multiply(number1, number2)

        elif operation == 'divide':
            if number2 == 0:
                result = "Cannot divide by zero"
            else:
                result = calc.divide(number1, number2)

    return render_template('index.html', result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

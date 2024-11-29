from flask import Flask, render_template, request
from currency import get_exchange_rate
import json

app = Flask(__name__)

with open("currencies.json") as f:
    currencies = json.load(f)

@app.route('/', methods=['GET', 'POST'])
def currency_converter():
    result = None
    if request.method == 'POST':
        from_currency = request.form['from_currency']
        to_currency = request.form['to_currency']
        amount = request.form['amount']

        try:
            conversion_result = get_exchange_rate(from_currency.lower(), to_currency.lower(), amount)
            result = f"{amount} {from_currency.upper()} = {conversion_result} {to_currency.upper()}"
        except KeyError as e:
            print(f"KeyError: {e}")
            result = "Invalid currency code selected."

    return render_template('index.html', currencies=currencies, result=result)

if __name__ == '__main__':
    app.run(debug=True)
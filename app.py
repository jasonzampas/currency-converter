from flask import Flask, render_template, request
from currency import get_exchange_rate
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def currency_converter():
    result = None

    with open("currencies.json") as f:
        currencies = json.load(f)
    
    if request.method == 'POST':
        from_currency = request.form['from_currency']
        to_currency = request.form['to_currency']
        amount = request.form['amount']

        try:
            conversion_result = get_exchange_rate(from_currency.lower(), to_currency.lower(), amount)
            
            from_name = currencies.get(from_currency.upper(), {}).get("name", "")
            from_symbol = currencies.get(from_currency.upper(), {}).get("symbol", "")
            to_name = currencies.get(to_currency.upper(), {}).get("name", "")
            to_symbol = currencies.get(to_currency.upper(), {}).get("symbol", "")
            
            result = f"{from_symbol}{amount} = {to_symbol}{conversion_result}"
        except KeyError as e:
            print(f"KeyError: {e}")
            result = "Invalid currency code selected."
    
    return render_template('index.html', currencies=currencies, result=result)

if __name__ == '__main__':
    app.run(debug=True)
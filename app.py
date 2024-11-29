from flask import Flask, render_template, request
from currency import get_exchange_rate

app = Flask(__name__)

currencies = {
    'EUR': 'Euro',
    'GBP': 'Pound Sterling',
    'JPY': 'Japanese Yen',
    'AUD': 'Australian Dollar',
    'CAD': 'Canadian Dollar',
    'CHF': 'Swiss Franc',
    'CNY': 'Chinese Yuan',
    'HKD': 'Hong Kong Dollar',
    'NZD': 'New Zealand Dollar',
    'INR': 'Indian Rupee',
    'MXN': 'Mexican Peso',
    'BRL': 'Brazilian Real',
    'RUB': 'Russian Ruble',
    'SEK': 'Swedish Krona',
    'SGD': 'Singapore Dollar',
    'KRW': 'South Korean Won',
    'ZAR': 'South African Rand',
    'NOK': 'Norwegian Krone',
    'TRY': 'Turkish Lira',
    'AED': 'UAE Dirham',
    'THB': 'Thai Baht',
    'DKK': 'Danish Krone',
    'PLN': 'Polish Zloty',
    'HUF': 'Hungarian Forint',
    'CZK': 'Czech Koruna',
    'ILS': 'Israeli New Shekel',
    'MYR': 'Malaysian Ringgit',
    'PHP': 'Philippine Peso',
    'SAR': 'Saudi Riyal',
    'EGP': 'Egyptian Pound',
    'VND': 'Vietnamese Dong',
    'IDR': 'Indonesian Rupiah',
    'COP': 'Colombian Peso',
    'PKR': 'Pakistani Rupee',
    'KWD': 'Kuwaiti Dinar',
    'BHD': 'Bahraini Dinar',
    'OMR': 'Omani Rial',
    'QAR': 'Qatari Rial',
    'KES': 'Kenyan Shilling',
    'BDT': 'Bangladeshi Taka',
    'MAD': 'Moroccan Dirham',
    'LKR': 'Sri Lankan Rupee',
    'RSD': 'Serbian Dinar',
    'ISK': 'Icelandic Krona',
    'JOD': 'Jordanian Dinar',
    'TWD': 'Taiwan Dollar',
    'UAH': 'Ukrainian Hryvnia'
}

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
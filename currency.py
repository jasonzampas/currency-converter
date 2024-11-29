import requests

def get_exchange_rate(from_currency, to_currency, amount):
    amount = float(amount)
    
    url = f"https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/{from_currency}.json"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()

        if to_currency in data[from_currency]:
            conversion = data[from_currency][to_currency]
            rate = round(conversion * amount, 2)

            return rate
        else:
            return f"Error: Conversion for {to_currency} not found."
    else:
        return f"Error: Failed to fetch data. Status code {response.status_code}."
import forex_python.converter

# Getting the user input for amount and currencies
amount = float(input("Enter the amount to convert: "))
from_currency = input("Enter the currency you're converting from (e.g., USD, EUR, GBP): ").upper()
to_currency = input("Enter the currency you're converting to: ").upper()

# Fetching exchange rates using forex_python
c = forex_python.converter.CurrencyRates()

try:
    # Perform the conversion
    converted_amount = c.convert(from_currency, to_currency, amount)

    # Display the result
    print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
except ValueError as e:
    print("Invalid currency code. Please check and try again.")

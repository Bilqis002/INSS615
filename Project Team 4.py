data = {
    "base": "USD",
    "date": "2023-12-15",
    "rates": {
        "EUR": 0.853,
        "USD": 1,
        "GBP": 0.740,
        "NGN": 1.100,
        "GHC": 0.985
    },
    "EUR":  {
        "USD": 1.17,
        "EUR": 1,
        "GBP": 0.723,
        "NGN": 1.020,
        "GHC": 0.993
    },
}
# a function to convert between currencies
def convert_currency(input_currency, output_currency, amount):
    # check if the input and output currencies are valid
    if input_currency in rates and output_currency in rates[input_currency]:
        # get the exchange rate from the dictionary
        rates = rates[input_currency][output_currency]
        # calculate the converted amount
        converted_amount = rates * amount
        # return the converted amount
        return converted_amount
    else:
        # return an error message
        return "Invalid currency code"
input_currency = int(input("Enter input_currency"))
print(convert_currency("USD", "EUR","converted_amount"))
print(convert_currency("GBP", "NGN", "converted_amount"))
print(convert_currency("USD", "GHC", "converted_amount"))
print(convert_currency("EUR", "GBP", "converted_amount"))


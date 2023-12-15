def main():
    print("this is the currency converter.")
    print("You can use these currency ('USD','EUR','GBP','JPY', 'NGN' ")

    amount = float(input("Enter the amount you want to convert :"))

    curr_currency = input("Enter the currency which you currently have :")
    want_currency = input("Enter the currency you want to have :")

    curr_currency= c.convert (amount,curr_currency,want_currency)
    # CurrencyConverter.convert()
    c = CurrencyConverter()

    print(f"The {amount} {curr_currency} in {want_currency} is :{converted_amount}")



_amount, _from_currency, _to_currency, = args
        amount, from_currency, to_currency = _amount.get(), _from_currency.get(), _to_currency.get()
        print(f'Amount: {amount}, From: {from_currency}, To: {to_currency}')

        if from_currency != 'USD':
            # Suppose I want to convert from EUR to AED.
            # Convert EUR to USD.
            usd = amount / self.rates[from_currency]
            # Convert USD to AED.
            amount = usd * self.rates[to_currency]
            print(amount)
        else:
            # In the case of the canonical currency itself, that rate will be 1.0
            amount = amount * self.rates[to_currency]
            print(amount)


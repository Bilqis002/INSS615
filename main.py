# import the modules
import requests
import argparse

# create an argument parser
parser = argparse.ArgumentParser(description="Currency converter using Fixer API")
# add the arguments
parser.add_argument("-i", "--input", type=str, required=True, help="The input currency code")
parser.add_argument("-o", "--output", type=str, required=True, help="The output currency code")
parser.add_argument("-a", "--amount", type=float, required=True, help="The amount to convert")
# parse the arguments
args = parser.parse_args()

# get the access key from the Fixer website
access_key = "YOUR_ACCESS_KEY"

# construct the API endpoint
endpoint = f"http://data.fixer.io/api/latest?access_key={access_key}&symbols={args.input},{args.output}"

# make the GET request
response = requests.get(endpoint)

# check the status code
if response.status_code == 200:
    # parse the JSON data
    data = response.json()
    # get the exchange rate
    rate = data["rates"][args.output] / data["rates"][args.input]
    # calculate the converted amount
    converted_amount = rate * args.amount
    # print the result
    print(f"{args.amount} {args.input} is equal to {converted_amount:.2f} {args.output}")
else:
    # print the error message
    print(f"Error: {response.status_code}")



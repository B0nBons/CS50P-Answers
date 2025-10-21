import requests
import sys


try:
    if len(sys.argv) == 1:
        print("Missing command-line argument" )
        sys.exit(1)
    if sys.argv[1].isalpha():
        sys.exit(1)
    parameters = {"bpi": "usd", "usd": "rate_float"}
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json', parameters)
    r = r.json()
    amount = (r["bpi"]["USD"]["rate_float"] )
    amount = amount * float(sys.argv[1])
    print(f"${amount:,.4f}")
    sys.exit(0)
except requests.exceptions.JSONDecodeError:
    print("Command-line argument is not a number")
    sys.exit(1)
sys.exit(1)

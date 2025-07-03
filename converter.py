import argparse
import sys

rates = {"USD": 0.2, "EUR": 1.2, "JPY": 5.2}

parse = argparse.ArgumentParser()
parse.add_argument("--amount", type=int)
parse.add_argument("--from", dest="from_currency", type=str)
parse.add_argument("--to", dest="to_currency", type=str)
parse.add_argument("--list", action="store_true")
parse.add_argument("--debug", action="store_true")
args = parse.parse_args()

if args.list:
    print(f"Supported currencies:", ", ".join(rates.keys()))
    sys.exit(0)

if args.amount is None or args.to_currency is None or args.from_currency is None:
    print(f"--amount, --to, --from is required unless --list")
    sys.exit(1)

from_currency = args.from_currency.upper()
to_currency = args.to_currency.upper()

if from_currency not in rates:
    print(
        f"{from_currency} is not in the options. The currency available are:",
        ", ".join(rates.keys()),
    )
    sys.exit(1)

if to_currency not in rates:
    print(
        f"{to_currency} is not in the options. The currency available are:",
        ", ".join(rates.keys()),
    )
    sys.exit(1)

amount_to_usd = args.amount * rates[from_currency]
converted = amount_to_usd * rates[to_currency]

if args.debug:
    print(f"Amount in USD: {amount_to_usd}")
    print(f"Converted amount in {to_currency}")


print(f"✅ {args.amount} {from_currency} = {converted} {to_currency}")

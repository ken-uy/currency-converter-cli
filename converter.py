import argparse
import sys


def main():
    # Parse CLI arguments
    parse = argparse.ArgumentParser()
    parse.add_argument("--amount", type=float)
    parse.add_argument("--from", dest="from_currency", type=str)
    parse.add_argument("--to", dest="to_currency", type=str)
    parse.add_argument("--list", action="store_true")
    parse.add_argument("--debug", action="store_true")
    args = parse.parse_args()

    # Define exchange rates
    rates = {"USD": 1, "EUR": 0.7, "JPY": 0.2}

    # If --list is used, display supported currencies and exit
    if args.list:
        print(f"Supported currencies:", ", ".join(rates.keys()))
        sys.exit(0)

    # Validate required inputs
    if args.amount is None or args.from_currency is None or args.to_currency is None:
        print(f"Error: --amount, --from, and --to are required (unless using list).")
        sys.exit(1)

    amount = args.amount
    from_currency = args.from_currency.upper()
    to_currency = args.to_currency.upper()

    # Validate supported currencies
    if from_currency not in rates:
        print(
            f"Error: {from_currency} is not supported, Choose from: {", ".join(rates.keys())}"
        )
        sys.exit(1)

    if to_currency not in rates:
        print(
            f"Error: {to_currency} is not supported, Choose from: {", ".join(rates.keys())}"
        )
        sys.exit(1)

    if amount <= 0:
        print(f"Error: Amount must be a positive number")
        sys.exit(1)

    # Perform currency conversion
    amount_in_usd = amount / rates[from_currency]
    converted = amount_in_usd * rates[to_currency]

    # Show result (with optional debug info)
    if args.debug:
        print(f"[DEBUG] Amount in USD: {amount_in_usd}")
        print(f"[DEBUG] Converted amount in {to_currency}: {converted}")

    print(f"{amount:.2f} {from_currency} = {converted:.2f} {to_currency}")


if __name__ == "__main__":
    main()

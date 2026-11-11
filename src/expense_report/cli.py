import argparse
import csv
from decimal import Decimal
from pathlib import Path

from .report import summarize


def main() -> None:
    parser = argparse.ArgumentParser(description="Total expenses by category.")
    parser.add_argument("csv_file", type=Path)
    args = parser.parse_args()
    try:
        totals = summarize(args.csv_file)
    except (OSError, ValueError, csv.Error) as error:
        parser.exit(1, f"Error: {error}\n")

    for category, total in sorted(totals.items()):
        print(f"{category}: {total:.2f}")
    print(f"Total: {sum(totals.values(), Decimal(0)):.2f}")


if __name__ == "__main__":
    main()

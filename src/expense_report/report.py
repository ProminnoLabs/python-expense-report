import csv
import re
from collections import defaultdict
from decimal import Decimal
from pathlib import Path


def summarize(path: Path) -> dict[str, Decimal]:
    totals: dict[str, Decimal] = defaultdict(Decimal)
    with path.open(newline="", encoding="utf-8-sig") as source:
        reader = csv.DictReader(source, strict=True)
        if reader.fieldnames != ["category", "amount"]:
            raise ValueError("Expected CSV header category,amount")

        for row in reader:
            category = (row["category"] or "").strip()
            amount = (row["amount"] or "").strip()
            if (
                None in row
                or not category
                or not re.fullmatch(r"[0-9]{1,12}(?:\.[0-9]{1,2})?", amount)
            ):
                raise ValueError(
                    f"Line {reader.line_num}: expected a category and a nonnegative "
                    "amount with up to 12 whole digits and two decimal places"
                )
            totals[category] += Decimal(amount)

    return dict(totals)

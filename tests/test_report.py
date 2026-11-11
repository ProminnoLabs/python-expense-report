import unittest
from decimal import Decimal
from pathlib import Path
from tempfile import TemporaryDirectory

from expense_report.report import summarize


class ExpenseReportTests(unittest.TestCase):
    def summarize_csv(self, content: str) -> dict[str, Decimal]:
        with TemporaryDirectory() as directory:
            source = Path(directory) / "expenses.csv"
            source.write_text(content, encoding="utf-8")
            return summarize(source)

    def test_adds_amounts_exactly(self) -> None:
        totals = self.summarize_csv("category,amount\nFood,0.10\nFood,0.20\nTravel,1\n")
        self.assertEqual(totals, {"Food": Decimal("0.30"), "Travel": Decimal("1")})

    def test_rejects_excess_decimal_places(self) -> None:
        with self.assertRaisesRegex(ValueError, "Line 2"):
            self.summarize_csv("category,amount\nFood,1.234\n")

    def test_rejects_unexpected_header(self) -> None:
        with self.assertRaisesRegex(ValueError, "Expected CSV header"):
            self.summarize_csv("amount,category\n1,Food\n")

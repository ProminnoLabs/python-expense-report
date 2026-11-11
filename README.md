# Python Expense Report

A Python CLI that validates a CSV of expenses and totals amounts by category using decimal arithmetic. Each file should use one currency.

Requires Python 3.10 or newer. In a virtual environment, run these commands from the repository root:

```sh
python -m pip install .
expense-report examples/sample.csv
python -m unittest discover -s tests -v
```

The sample totals 18.25 for Food and 12.00 for Travel. The `src/expense_report` package separates CSV parsing and aggregation from argument handling and output. `tests/` covers exact arithmetic and invalid input.

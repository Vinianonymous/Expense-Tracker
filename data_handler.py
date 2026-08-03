import csv

FIELDS = ["id", "name", "date", "amount"]


def load_data():
    try:
        with open("expenses.csv", "r", newline="") as f:
            return list(csv.DictReader(f))
    except FileNotFoundError:
        with open("expenses.csv", "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDS)
            writer.writeheader()
        return []


def write_data(data):
    with open("expenses.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(data)

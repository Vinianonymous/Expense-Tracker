from csv import DictReader, DictWriter


def load_data():
    with open("expenses.csv", "r") as f:
        fields = ["id", "date", "description", "amount"]
        reader = DictReader(f, fieldnames=fields)
        expenses = list(reader)
        expenses.remove(expenses[0])  # Remove the header row
        return expenses


def write_data(data: dict):
    with open("expenses.csv", "a", newline="") as f:
        fields = ["id", "date", "description", "amount"]
        writer = DictWriter(f, fieldnames=fields)
        writer.writerow(data)

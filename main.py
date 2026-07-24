from argparse import ArgumentParser
from data_handler import load_data, write_data


def list_expenses(expenses: list):
    print("ID\t Date\t Description\t Amount")
    for expense in expenses:
        print(
            f"{expense['id']}\t {expense['date']}\t {expense['description']}\t\t ${expense['amount']}"
        )


def main():
    expenses = load_data()
    parser = ArgumentParser(description="Expense Tracker")
    parser.add_argument("--list", action="store_true", help="List all expenses")
    args = parser.parse_args()
    if args.list:
        list_expenses(expenses)


if __name__ == "__main__":
    main()

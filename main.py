from argparse import ArgumentParser
from data_handler import load_data, write_data

def list_expenses(expenses):
    print("ID\tName\tDate\t\tAmount")
    for expense in expenses:
        print(
            f"{expense['id']}\t{expense['name']}\t{expense['date']}\t${expense['amount']}"
        )


def add_expense(expenses, expense):
    expenses.append(expense)
    write_data(expenses)


def main():
    expenses = load_data()

    parser = ArgumentParser(description="Expense Tracker")
    subparsers = parser.add_subparsers(dest="command")

    # add
    add = subparsers.add_parser("add")
    add.add_argument("name")
    add.add_argument("date")
    add.add_argument("amount", type=float)

    # list
    list_parser = subparsers.add_parser("list")

    # remove
    remove = subparsers.add_parser("remove")
    remove.add_argument("id", type=int)

    args = parser.parse_args()

    if args.command == "list":
        list_expenses(expenses)

    elif args.command == "add":
        next_id = max((int(expense["id"]) for expense in expenses), default=0) + 1

        expense = {
            "id": next_id,
            "name": args.name,
            "date": args.date,
            "amount": args.amount,
        }

        add_expense(expenses, expense)

    elif args.command == "remove":
        expenses = [
            expense
            for expense in expenses
            if int(expense["id"]) != args.id
        ]
        write_data(expenses)

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
# budget_tracker.py
# Personal Budget Tracker

import json
import os
import uuid
from datetime import date

# ----------------------------
# Data storage
# ----------------------------
transactions = []

INCOME_CATEGORIES = ["Job", "Freelance", "Gift", "Financial aid", "Other"]
EXPENSE_CATEGORIES = ["Food", "Rent", "Transportation", "Entertainment", "School", "Health", "Other"]

DATA_FILE = "budget_data.json"


# ----------------------------
# Save / Load
# ----------------------------
def save_data():
    with open(DATA_FILE, "w") as f:
        json.dump(transactions, f, indent=4)
    print("  Data saved successfully!")


def load_data():
    global transactions

    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as f:
                transactions = json.load(f)
            print("  Data loaded successfully!")
        except (json.JSONDecodeError, FileNotFoundError):
            transactions = []
    else:
        transactions = []


# ----------------------------
# Add Income
# ----------------------------
def add_income():
    print("\n-- Add Income --")

    for i, cat in enumerate(INCOME_CATEGORIES, 1):
        print(f"  {i}. {cat}")

    choice = input("Pick a category (number): ").strip()

    if not choice.isdigit() or not (1 <= int(choice) <= len(INCOME_CATEGORIES)):
        print("  Invalid choice.")
        return

    category = INCOME_CATEGORIES[int(choice) - 1]

    amount = input("Enter amount: $").strip()

    try:
        amount = float(amount)
        if amount <= 0:
            print("  Amount must be greater than 0.")
            return
    except ValueError:
        print("  Invalid number.")
        return

    note = input("Add a note (optional): ").strip()

    transaction = {
        "id": str(uuid.uuid4())[:8],
        "type": "income",
        "category": category,
        "amount": round(amount, 2),
        "note": note,
        "date": str(date.today())
    }

    transactions.append(transaction)
    print(f"  Added income: +${amount:.2f} ({category})")


# ----------------------------
# Add Expense
# ----------------------------
def add_expense():
    print("\n-- Add Expense --")

    for i, cat in enumerate(EXPENSE_CATEGORIES, 1):
        print(f"  {i}. {cat}")

    choice = input("Pick a category (number): ").strip()

    if not choice.isdigit() or not (1 <= int(choice) <= len(EXPENSE_CATEGORIES)):
        print("  Invalid choice.")
        return

    category = EXPENSE_CATEGORIES[int(choice) - 1]

    amount = input("Enter amount: $").strip()

    try:
        amount = float(amount)
        if amount <= 0:
            print("  Amount must be greater than 0.")
            return
    except ValueError:
        print("  Invalid number.")
        return

    note = input("Add a note (optional): ").strip()

    transaction = {
        "id": str(uuid.uuid4())[:8],
        "type": "expense",
        "category": category,
        "amount": round(amount, 2),
        "note": note,
        "date": str(date.today())
    }

    transactions.append(transaction)
    print(f"  Added expense: -${amount:.2f} ({category})")


# ----------------------------
# View Transactions
# ----------------------------
def view_transactions():
    print("\n-- Transactions --")

    if not transactions:
        print("  No transactions yet.")
        return

    for t in transactions:
        sign = "+" if t["type"] == "income" else "-"
        note = f" | Note: {t['note']}" if t["note"] else ""

        print(f"[{t['date']}] ID:{t['id']} | {t['type']} | {t['category']} | {sign}${t['amount']:.2f}{note}")


# ----------------------------
# Summary
# ----------------------------
def view_summary():
    print("\n-- Summary --")

    if not transactions:
        print("  Nothing to summarize.")
        return

    income = 0
    expense = 0
    categories = {}

    for t in transactions:
        if t["type"] == "income":
            income += t["amount"]
        else:
            expense += t["amount"]
            categories[t["category"]] = categories.get(t["category"], 0) + t["amount"]

    balance = income - expense

    print(f"Total Income:   +${income:.2f}")
    print(f"Total Expenses: -${expense:.2f}")
    print(f"Balance:         ${balance:.2f}")

    if categories:
        print("\nSpending by Category:")
        for c, v in categories.items():
            print(f"  {c}: ${v:.2f}")

    if balance < 0:
        print("\n⚠ You're in the negative.")
    else:
        print("\nYou're in the green!")


# ----------------------------
# Delete transaction
# ----------------------------
def delete_transaction():
    view_transactions()

    if not transactions:
        return

    entry_id = input("\nEnter ID to delete: ").strip()

    for i, t in enumerate(transactions):
        if t["id"] == entry_id:
            removed = transactions.pop(i)
            print(f"Deleted {removed['type']} {removed['category']} ${removed['amount']}")
            return

    print("No transaction found.")


# ----------------------------
# Export report
# ----------------------------
def export_report():
    filename = f"budget_report_{date.today()}.txt"

    income = 0
    expense = 0

    with open(filename, "w") as f:
        f.write("BUDGET REPORT\n\n")

        for t in transactions:
            sign = "+" if t["type"] == "income" else "-"
            f.write(f"{t['date']} | {t['type']} | {t['category']} | {sign}${t['amount']:.2f}\n")

            if t["type"] == "income":
                income += t["amount"]
            else:
                expense += t["amount"]

        f.write("\n------------------\n")
        f.write(f"Income: +${income:.2f}\n")
        f.write(f"Expenses: -${expense:.2f}\n")
        f.write(f"Balance: ${income - expense:.2f}\n")

    print(f"  Exported to {filename}")


# ----------------------------
# Main Program
# ----------------------------
def main():
    print("=======================")
    print(" Personal Budget Tracker")
    print("=======================")

    load_data()

    while True:
        print("\n1. Add Income")
        print("2. Add Expense")
        print("3. View Transactions")
        print("4. View Summary")
        print("5. Delete Transaction")
        print("6. Export Report")
        print("7. Save & Quit")

        choice = input("Choose (1-7): ").strip()

        if choice == "1":
            add_income()
        elif choice == "2":
            add_expense()
        elif choice == "3":
            view_transactions()
        elif choice == "4":
            view_summary()
        elif choice == "5":
            delete_transaction()
        elif choice == "6":
            export_report()
        elif choice == "7":
            save_data()
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()


    

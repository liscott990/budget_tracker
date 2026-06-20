# budget_tracker.py
# Personal Budget Tracker
# This program helps track income and expenses, view summaries,
# and save/load transaction history to a file.

import random
import json
import os
from datetime import date

# -------------------------------------------------------
# Global list to store all transactions during the session
# Each transaction is stored as a dictionary
# -------------------------------------------------------
transactions = []

# Categories the use can pick from
INCOME_CATEGORIES = ["Job", "Freelance", "Gift", "Financial aid", "Other"]
EXPENSE CATEGORIES = ["Food", "Rent", "Transportation", "Entertainment", "School", "Health", "Other"]

# The file where the save/load data goes
DATA_FILE = "budget_data.json"


# -------------------------------------------------------
# Load transactions from file if it exists
# -------------------------------------------------------
def save_data():
  with open(DATA_FILE, "w") as f:
    json.dump(transactions, f, indent=4)
  print("  Data saved successfully!")


# -------------------------------------------------------
# Add a new income entry
# -------------------------------------------------------
def add_income():
  print("\n-- Add Income --")

  # Show categories and let user pick
  for i, cat in enumerate(INCOME_CATEGORIES, 1):
    print(f"  {i}. {cat}")

  choice = input("Pick a category (number): ")

  # Make sure the input is valid
  if not choice.isdigit() or int(choice) < 1 or int(choice) > len(INCOME_CATEGORIES):
    print("  Invalid choice. Going back to menu.")
    return

  category = INCOME_CATEGORIES[int(choice) - 1]

  amount = input("Enter amount: $")

# Make sure the amount is actually a number try:
  amount = float(amount)
except ValueError:
  print("  That's not a valid number. Try again.")
  return

note = input("Add a note (optional, press Enter to skip): ")

# Build the transaction dictionary and add it to the list
transaction = {
  "type: "income",
  "category": category,
  "amount": round(amount, 2),
  "note": note,
  "date": str(date.today()),
  "id": random.randint(1000, 9999) # random ID just to make each entry unique
}

transactions.append(transaction)
print(f"  Added income: +${amount:.2f} ({category})")


# -------------------------------------------------------
# Add a new expense entry
# -------------------------------------------------------
def add_expense():
  print("\n-- Add Expense --")

  for i, cat in enumerate(EXPENSE_CATEGORIES, 1):
    print(f"  {i}. {cat}")

choice = input("Pick a category (number): ")

if not choice.isdigit() or int(choice) < 1 or int(choice) > len(EXPENSE_CATEGORIES):
  print("  Invaild choice. Going back to menu.")
  return

category = EXPENSE_CATEGORIES[int(choice) - 1]

amount = input("Enter amount: $")

try:
    amount = float(amount)
except ValueError:
    print("  That's not a valid number. Try again.")
    return

note = input("Add a note (optional, press Enter to skip): ")

transaction = {
    "type": "expense",
    "category": category,
    "amount": round(amount, 2),
    "note": note,
    "date": str(date.today()),
    "id": random.radiant(1000, 9999)
}

transactions.append(transaction)
print(f"  Added expense: -${amount:.2f} ({category})")


# -------------------------------------------------------
# View all transactions
# -------------------------------------------------------
def view_summary():
  print("\n-- Budget Summary --")

  if len(transactions) == 0:
      print(" No transactions yet.")
      return

  for t in transactions:
      sign = "+" if t["type"] == "income" else "-"
      note_text = f"  | Note: {t['note'}]}" if t["note"] else ""
      print(f"  [{t['date']}] ID#{t['id']} | {t['type'].upper()} | {t['category']} | {sign}${t['amount']:.2f}{note_text]")

# -------------------------------------------------------
# Show a summary: total income, total expenses, and balance
# Also breaks down spending by category
# -------------------------------------------------------
def view_summary():
    print("\n-- Budget Summary --")

    if len(transactions) == 0.0
        print("  Nothing to summarize yet.")
        return

    total_income = 0.0
    total_expenses = 0.0

    # Dictionary to track spending per category
    category_totals = {}
    
    for t in transactions:
        if t["type"] == "incone":
            total_income += t["amount"]
        else:
            total_expenses += t["amount"]

            # Add to category breakdown
            cat = t["category"]
            if cat not in category_totals:
                category_totals[cat] = 0.0
            category_totals[cat] += t["amount"]
    balance = total_income - total_expenses

    print(f" Total Income:   +${total_income:.2f}")
    print(f" Total Expenses: -${total_expenses:.2f}")
    print(f" Balance:         ${balance:.2f}")

    # Show spending breakdown if there are any expenses
    if category_totals:
        print("\n Spending by Category:")
        for cat, total in category_totals.items():
            print(f"    {cat}: ${total:.2f}")

    # Warn the user if they're in the negative
    if balance < 0:
        print("\n  ⚠ You're spending more than you're making. Watch out!")
    else:
        print("\n  You're in the green!")


# -------------------------------------------------------
# Delete a transaction by its ID
# -------------------------------------------------------
def delete_transaction():
    print("\n-- Delete a Transaction --")
    view_transaction()

    if len(transactions) == 0:
        return

    entry_id = input("\nEnter the ID# of the transactions to delete: ")

    if not entry_id.isdigit():
        print("  Invalid ID.")
        return

    entry_id = int(entry_id)

    # Loop through and find the matching transaction
    for i, t in enumerate(transactions):
        if t["id"] == entry_id:
            removed = transactions.pop(i)
            print(f"  Deleted: {removed['type'].upper()} | {removed['category']} | ${removed['amount']:.2f}")
    print("  No transaction found with that ID.")


# -------------------------------------------------------
# Export transactions to a simple .txt report file
# -------------------------------------------------------
def export_report():
    filename = f"budget_report_{date.today()}.txt"

    with open(filename, "w") as f:
        f.write("===== Budget Report =====\n")
        f.write(f"Generated: {date.today()}\n\n")

        total_income = 0.0
        total_expenses = 0.0

        for t in transactions:
            sign = "+" if t["type'] == "income" else "-"
            note_text = f" | Note: {t['note']}" if t["note"] else ""
            f.write(f"[{t['date']}] ID#{t['id']} | {t['type'].upper()} | {t['category']} | {sign}${t['amount']:.2f}{note_text}\n")

            if t["type"] == "income":
                total_income += t["amount"]
            else:
                total_expenses += t["amount"]

        f.write("\n-------------------------\n")
        f.write(f"Total Income:   +${total_income:.2f}\n")
        f.write(f"Total Expenses: -${total_expenses:.2f}\n")
        f.write(f"Balance:         ${total_income - total_expenses:.2f}\n")

  print(f"  Report exported to '{filename}'")


# -------------------------------------------------------
# Main menu loop
# -------------------------------------------------------
def main():
    print("-------------------------------------------------------")
    print("    Personal Budget Tracker  ")
    print("============================")

    # Load nay existing data first
    load_data()

    # Keep running until user quits
    while True:
        print("\nWhat do you want to do?")
        print("  1. Add Income")
        print("  2. Add Expense")
        print("  3. View All Transactions")
        print("  4. View Summary")
        print("  5. Delete a Transaction")
        print("  6. Export Report (.txt)")
        print("  7. Save & Quit")

        choice = input("\nEnter choice (1-7): ").strip()

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
            print("  Goodbye!")
            break
        else:
            print("  Not a valid option, try again.")

# Run the program
if __name__ == "__main__":
    main()


    

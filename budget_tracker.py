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

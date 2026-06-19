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

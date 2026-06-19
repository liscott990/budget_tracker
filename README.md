# Personal Budget Tracker
Personal budget tracker that lets users add income and expenses, organize them, and look back at their transactions.
See there your money is going, and save everything so it's there next time you open it.
---
## About
I built this as a mini Python project for class. The idea was to make something useful, a program that helps you manage your money without needing an app or spreadsheet. You can log transactions, view a summary of your balance, and export a report as a text file.
---
## Features
- Add income and expenses across multiple categories
- View all transactions with dates and IDs
- See a full summary
- Spending breakdown by category
- Auto saves data to a file so nothing is lost between sessions
- Export a readable `.txt` report
- Delete transactions by ID
---
## Concepts used
- Functions
- Lists & Dictionaries
- While and For loops
- File read/write
- Random number generator
- User input handling
---
## How to run
1. Make sure Python is installed
2. Clone or download this repo
3. Run the program:
   - Open Command Prompt
   - Navigate to the folder where you saved the file:
     `bash cd Downloads`, then run it: bash python budget_tracker.py
5. On Mac:
   - Open Terminal
   - Navigate to the folder:
     `bash cd Downloads`, then run it: bash python3 budget_tracker.py
---
## Files
| File                          | Purpose                                                        |
|-------------------------------|----------------------------------------------------------------|
| `budget_tracker.py`           | The main program.                                              |
| `budget_data.json`            | Auto-generates save file                                       |
| `budget_report_YYY-MM-DD.txt` | Exported report (generated when you choose option 6            |

import json
import os
from datetime import datetime

FILE_NAME = "expenses.json"

# -------------------- Load Data --------------------
def load_data():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return json.load(file)

# -------------------- Save Data --------------------
def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

# -------------------- Add Expense --------------------
def add_expense():
    data = load_data()

    try:
        date = input("Enter date (YYYY-MM-DD): ")
        datetime.strptime(date, "%Y-%m-%d")  # validation

        category = input("Enter category (Food/Travel/Shopping/etc): ")
        amount = float(input("Enter amount: "))
        if amount <= 0:
            print("Amount must be greater than 0")
            return

        description = input("Enter description: ")

        expense_id = len(data) + 1

        expense = {
            "id": expense_id,
            "date": date,
            "category": category,
            "amount": amount,
            "description": description
        }

        data.append(expense)
        save_data(data)

        print("Expense added successfully!")

    except ValueError:
        print("Invalid input format!")

# -------------------- View Expenses --------------------
def view_expenses():
    data = load_data()

    if not data:
        print("No expenses found.")
        return

    print("\n--- Expense List ---")
    print("{:<5} {:<12} {:<12} {:<10} {:<20}".format(
        "ID", "Date", "Category", "Amount", "Description"
    ))

    for exp in data:
        print("{:<5} {:<12} {:<12} {:<10} {:<20}".format(
            exp["id"], exp["date"], exp["category"],
            exp["amount"], exp["description"]
        ))

# -------------------- Delete Expense --------------------
def delete_expense():
    data = load_data()

    try:
        exp_id = int(input("Enter Expense ID to delete: "))

        new_data = [exp for exp in data if exp["id"] != exp_id]

        if len(new_data) == len(data):
            print("Expense ID not found!")
            return

        # reassign IDs
        for i, exp in enumerate(new_data, start=1):
            exp["id"] = i

        save_data(new_data)
        print("Expense deleted successfully!")

    except ValueError:
        print("Invalid ID!")

# -------------------- Total Expense --------------------
def total_expense():
    data = load_data()
    total = sum(exp["amount"] for exp in data)
    print(f"\nTotal Expense: ₹{total}")

# -------------------- Category Summary --------------------
def category_summary():
    data = load_data()

    summary = {}

    for exp in data:
        cat = exp["category"]
        summary[cat] = summary.get(cat, 0) + exp["amount"]

    print("\n--- Category Wise Summary ---")
    for cat, amt in summary.items():
        print(f"{cat}: ₹{amt}")

# -------------------- Menu --------------------
def menu():
    while True:
        print("\n===== EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Total Expense")
        print("5. Category Summary")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            delete_expense()
        elif choice == "4":
            total_expense()
        elif choice == "5":
            category_summary()
        elif choice == "6":
            print("Exiting... Stay financially smart 💡")
            break
        else:
            print("Invalid choice! Try again.")

# -------------------- Run Program --------------------
menu()
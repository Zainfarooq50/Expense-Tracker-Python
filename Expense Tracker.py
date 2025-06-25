expenses = []

def add_expense():
    description = input("Enter expense description: ")
    try:
        amount = float(input("Enter expense amount: "))
    except ValueError:
        print("Invalid input. Please try again.")
        return

    expenses.append({"description": description, "amount": amount})
    save_expenses_to_file()
    print("Expense added successfully!\n")

def view_expenses():
    if not expenses:
        print("No expenses recorded.\n")
        return
    for idx, expense in enumerate(expenses, start=1):
        print(f"{idx}. {expense['description']} - {expense['amount']} PKR")
    print()

def show_total_expenses():
    total = sum(exp["amount"] for exp in expenses)
    print(f"Total spent: {total} PKR\n")

def delete_expense():
    if not expenses:
        print("No expenses to delete.\n")
        return
    view_expenses()
    try:
        idx = int(input("Enter index of expense to delete: "))
        if idx < 1 or idx > len(expenses):
            print("Invalid input. Please try again.")
            return
    except ValueError:
        print("Invalid input. Please try again.")
        return

    removed = expenses.pop(idx - 1)
    save_expenses_to_file()
    print(f"Expense deleted successfully! {removed['description']} - {removed['amount']} PKR\n")

def edit_expense():
    if not expenses:
        print("No expenses to edit.\n")
        return

    view_expenses()

    try:
        idx = int(input("Enter expense number to edit: "))
        if idx < 1 or idx > len(expenses):
            print("Invalid input. Please try again.\n")
            return
    except ValueError:
        print("Invalid input. Please try again.\n")
        return

    expense = expenses[idx - 1]

    print(f"Current description: {expense['description']}")
    new_description = input("Enter new description (press enter to keep current): ")
    if new_description:
        expense["description"] = new_description

    print(f"Current amount: {expense['amount']} PKR")

    new_amount_input = (input("Enter new amount (press enter to keep current): "))
    if new_amount_input:
        try:
            expense["amount"] = float(new_amount_input)
        except ValueError:
            print("Invalid input. Keep current amount.\n.")

    save_expenses_to_file()
    print("Expense updated successfully!\n")



def save_expenses_to_file():
    with open("expenses.txt", "w") as file:
        for expense in expenses:
            file.write(f"{expense['description']},{expense['amount']}\n")

def load_expenses_from_file():
    try:
        with open("expenses.txt", "r") as file:
            for line in file:
                description, amount = line.strip().split(",")
                expenses.append({"description": description, "amount": float(amount)})
    except FileNotFoundError:
        pass

load_expenses_from_file()
while True:
    print("Welcome to Expense Tracker!")
    print("[1] Add expense")
    print("[2] View expenses")
    print("[3] Show total spent")
    print("[4] Delete expense")
    print("[5] Edit expense")
    print("[6] Exit")

    choice = input("Enter your choice: ")


    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        show_total_expenses()
    elif choice == "4":
        delete_expense()
    elif choice == "5":
        edit_expense()
    elif choice == "6":
        print("Thank you for using Expense Tracker. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.\n")


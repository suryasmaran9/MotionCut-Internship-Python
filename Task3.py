
#Expense Tracker

import datetime

expenses = {}

def add_expense(amount, description, category):

    today = datetime.date.today()
    month_year = f"{today.month}-{today.year}"
    
    if month_year not in expenses:
        expenses[month_year] = []
    
    expenses[month_year].append((amount, description, category))
    print("Expense added successfully!")

def show_monthly_summary():

    month_year = input("Enter month-year (e.g., 5-2024 for May 2024): ")
    
    if month_year in expenses:
        total_expenses = sum(amount for amount, _, _ in expenses[month_year])
        print(f"Total expenses for {month_year}: ${total_expenses:.2f}")
    else:
        print("No expenses found for the specified month.")

def show_category_summary():

    category = input("Enter expense category (e.g., food, transportation): ")
    
    total_category_expenses = 0
    for expenses_list in expenses.values():
        for amount, _, cat in expenses_list:
            if cat.lower() == category.lower():
                total_category_expenses += amount
    
    print(f"Total expenses for {category}: ${total_category_expenses:.2f}")

def main():

    print("Welcome to the Expense Tracker!")
    
    while True:
        print("\nChoose an option:")
        print("1. Add an expense")
        print("2. Show monthly summary")
        print("3. Show category-wise summary")
        print("4. Exit")
        
        choice = input("Enter your choice (1/2/3/4): ")
        
        if choice == "1":
            amount = float(input("Enter the amount spent: "))
            description = input("Enter a brief description: ")
            category = input("Enter expense category: ")
            add_expense(amount, description, category)
        
        elif choice == "2":
            show_monthly_summary()
        
        elif choice == "3":
            show_category_summary()
        
        elif choice == "4":
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()

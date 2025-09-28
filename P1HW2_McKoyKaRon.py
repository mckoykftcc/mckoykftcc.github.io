# -------------------------------------------
# Name: [Your Name]
# Date: 09/28/2025
# Assignment Name: Travel Budget Calculator
# Description: This program asks the user for their travel budget and 
#              planned expenses (gas, accommodation, and food), then 
#              calculates the total expenses and remaining budget. 
#              It also displays the destination and final results.
# -------------------------------------------

# Ask for budget and destination
budget = float(input("Enter your total travel budget: "))
destination = input("Enter your travel destination: ")

# Ask for individual expenses
gas = float(input("Enter the amount you will spend on gas: "))
accommodation = float(input("Enter the amount you will spend on accommodation: "))
food = float(input("Enter the amount you will spend on food: "))

# Add expenses
total_expenses = gas + accommodation + food

# Subtract expenses from budget
remaining_budget = budget - total_expenses

# Display results
print("\n--------Travel Summary--------")
print(f"Destination: {destination}")
print(f"Initial Budget: ${budget:.2f}")
print(f"Total Expenses: ${total_expenses:.2f}")
print(f"Remaining Budget: ${remaining_budget:.2f}")

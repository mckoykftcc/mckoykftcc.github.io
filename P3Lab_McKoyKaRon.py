# -------------------------------------------
# Name: KaRon McKoy
# Date: 10/17/2025
# Assignment Name: P3LAB_LastnameFirstname
# Description: This program asks the user to enter a money amount and calculates the most efficient number of dollars, quarters, dimes, nickels, and pennies needed to make that amount.
# -------------------------------------------

# Ask the user for a money amount
amount = float(input("Enter the amount of money (e.g., 12.34): "))

# Convert amount to cents to simplify calculations
cents = int(round(amount * 100))

# Compute dollars
dollars = cents // 100
cents -= dollars * 100

# Compute quarters
quarters = cents // 25
cents -= quarters * 25

# Compute dimes
dimes = cents // 10
cents -= dimes * 10

# Compute nickels
nickels = cents // 5
cents -= nickels * 5

# Remaining cents are pennies
pennies = cents

# Function to format singular/plural
def format_coin(count, singular, plural):
    if count == 0:
        return ""
    elif count == 1:
        return f"{count} {singular}"
    else:
        return f"{count} {plural}"

# Prepare output
output_parts = [
    format_coin(dollars, "dollar", "dollars"),
    format_coin(quarters, "quarter", "quarters"),
    format_coin(dimes, "dime", "dimes"),
    format_coin(nickels, "nickel", "nickels"),
    format_coin(pennies, "penny", "pennies")
]

# Filter out empty strings and join with commas
output = ", ".join(part for part in output_parts if part)

# Display the result
print(output)

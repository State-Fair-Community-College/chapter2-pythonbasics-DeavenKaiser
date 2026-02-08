# --------------------------------------------
# Name:deav
# Date:
# Program: Chapter 2 Practice – Answer Key
# Description:
# Demonstrates variables, input, calculations,
# and formatted output in Python.
# --------------------------------------------

# ------------------------------------------------
# Practice 1: Variables and print
# ------------------------------------------------
name = "Your Name"
print("Hello,", name)

print()  # blank line for readability


# ------------------------------------------------
# Practice 2: Input and output
# ------------------------------------------------
favorite_color = input("Enter your favorite color: ")
print("Your favorite color is", favorite_color)

print()


# ------------------------------------------------
# Practice 3: Adding two numbers
# ------------------------------------------------
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

total = num1 + num2
print("The total is", total)

print()


# ------------------------------------------------
# Practice 4: Calculations with variables
# ------------------------------------------------
price = float(input("Enter the price of an item: "))
TAX_RATE = 0.08

tax = price * TAX_RATE
final_price = price + tax

print("Final price:", final_price)

print()


# ------------------------------------------------
# Practice 5: Formatted output with f-strings
# ------------------------------------------------
hours_worked = float(input("Enter hours worked: "))
hourly_pay = float(input("Enter hourly pay: "))

weekly_pay = hours_worked * hourly_pay

print(f"You earned ${weekly_pay:.2f} this week.")

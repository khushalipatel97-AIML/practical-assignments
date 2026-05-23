# 20. Write a program to invalid input using exception handling.
try:
    num = int(input("Enter a number: "))
    print("You entered:", num)

except ValueError:
    print("Error: Invalid input. Please enter a valid number.")
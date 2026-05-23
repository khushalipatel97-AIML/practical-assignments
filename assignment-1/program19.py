# 19. Write a program to division by zero error.
try:
    num1 = 10
    num2 = 0

    result = num1 / num2
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
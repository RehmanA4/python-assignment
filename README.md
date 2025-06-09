# python-assignment
# Taking two numbers as input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Performing basic mathematical operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2

# Displaying the results
print("\nResults:")
print(f"Addition: {num1} + {num2} = {addition}")
print(f"Subtraction: {num1} - {num2} = {subtraction}")
print(f"Multiplication: {num1} × {num2} = {multiplication}")
print(f"Division: {num1} ÷ {num2} = {division}")
'''the output:
Enter the first number: 15
Enter the second number: 20

Results:
Addition: 15.0 + 20.0 = 35.0
Subtraction: 15.0 - 20.0 = -5.0
Multiplication: 15.0 × 20.0 = 300.0
Division: 15.0 ÷ 20.0 = 0.75

Process finished with exit code 0'''

#task2
# Taking user's first name and last name as input
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

# Concatenating the first name and last name into a full name
full_name = first_name + last_name

# Printing a personalized greeting message
print(f"\nHello, {full_name}! Welcome! to the world of python")

'''the output:
Enter your first name: mohammad
Enter your last name: abdul rehman

Hello, mohammad abdul rehman! Welcome! to the world of python

Process finished with exit code 0'''

#task 1
# # Taking an integer input from the user
num = int(input("Enter a number: "))

# Checking whether the number is even or odd
if num % 2 == 0:
    print(f"{num} is an even number.")
else:
    print(f"{num} is an odd number.")

    '''the output 1
    enter a number: 5
    5 is an odd number 
       the output 2
       enter a number: 6
    6 is an even number  '''

#task 2;
# Initialize the sum variable
total_sum = 0

# Iterate over numbers from 1 to 50
for num in range(1, 51):
    total_sum += num  # Add each number to total_sum

# Display the final sum
print(f"The sum of numbers from 1 to 50 is: {total_sum}")


'''the output:
The sum of numbers from 1 to 50 is: 1275'''
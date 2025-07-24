# lambda Function
# List of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use a lambda function to filter out odd numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))

# Use a lambda function to square each number
squares = list(map(lambda x: x ** 2, numbers))

# Print the results
print("Original numbers:", numbers)
print("Even numbers:", evens)
print("Squared numbers:", squares)

# Try creating your own lambda function!
# Uncomment and modify the line below:
your_result = list(map(lambda x: x ** 3 <= 500, numbers))
print("Your result:", your_result)

# map Function

# Sample list of names
names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']

# Using map with a lambda function to get the length of each name
name_lengths = list(map(lambda x: len(x), names))

# Using map with a defined function to capitalize each name
def capitalize_name(name):
    return name.upper()

capitalized_names = list(map(capitalize_name, names))

# Print the results
print("Original names:", names)
print("Name lengths:", name_lengths)
print("Capitalized names:", capitalized_names)

# Try creating your own map function!
# Uncomment and modify the line below:
your_result = list(map(lambda x: x[2], names))
print("Your result:", your_result)





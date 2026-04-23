#Write a program to demonstrate list slicing and list manipulation.


numbers = [10, 20, 30, 40, 50, 60]
print("Original List:", numbers)

# List Slicing
print("\nSlicing examples:")
print("First 3 elements:", numbers[0:3])

# List Manipulation
print("\nList Manipulation:")

# Add element
numbers.append(70)
print("After append:", numbers)

# Insert element
numbers.insert(2, 25)
print("After insert at index 2:", numbers)

# Remove element
numbers.remove(40)
print("After removing 40:", numbers)

# Update element
numbers[1] = 200
print("After updating index 1:", numbers)

# Delete element
del numbers[3]
print("After deleting index 3:", numbers)
#Write a program to perform tuple operations and demonstrate immutability.

# Initialization
my_tuple = (10, 20, 30, 40, 50)
another_tuple = ("Python", 3.11, True)

print("--- Tuple Operations ---")

# Indexing and Slicing
print(f"First element: {my_tuple[0]}")
print(f"Last element: {my_tuple[-1]}")
print(f"Slice (indices 1 to 3): {my_tuple[1:4]}")

#  Concatenation and Repetition
combined = my_tuple + another_tuple
multiplied = ("A", "B") * 3
print(f"Concatenated: {combined}")
print(f"Repeated: {multiplied}")


# 5. Built-in Methods
print(f"Index of 'Python': {another_tuple.index('Python')}")
print(f"Count of 20: {my_tuple.count(20)}")

# --- Demonstrating Immutability ---
print("\n--- Demonstrating Immutability ---")
print(f"Original tuple: {my_tuple}")

try:
    # Attempting to change an element
    my_tuple[1] = 99
except TypeError as e:
    print(f"Error caught: {e}")
    print("Verification: You cannot modify a tuple after creation.")

# Note: You can "update" by creating a new tuple (re-assignment)

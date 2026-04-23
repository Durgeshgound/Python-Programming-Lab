#Write a program to iterate through string, list, and dictionary using loops.

# Iterate through a string
text = "Hello"

print("Iterating through string:")
for char in text:
    print(char)

# Iterate through a list
numbers = [10, 20, 30, 40]

print("\nIterating through list:")
for num in numbers:
    print(num)

# Iterate through a dictionary
student = {
    "Name": "Durgesh",
    "Age": 20,
    "Course": "BCA"
}
print("\nIterating through dictionary (key-value pairs):")
for key, value in student.items():
    print(key, ":", value)
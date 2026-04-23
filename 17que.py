# Write a program to read contents of a file using read(), readline(),and readlines().# Open file in read mode

# Open the file in read mode
file = open("example.txt", "r")

# 1. Using read()
print("Using read():")
content = file.read()
print(content)

# Move file pointer to beginning
file.seek(0)

# 2. Using readline()
print("\nUsing readline():")
line1 = file.readline()
line2 = file.readline()
print(line1)
print(line2)

# Move file pointer to beginning
file.seek(0)

# 3. Using readlines()
print("\nUsing readlines():")
lines = file.readlines()
print(lines)

# Close the file
file.close()
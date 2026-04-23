#Write a program to copy contents of one file to another.

# Copy contents from one file to another

# Open source file in read mode
source = open("example.txt", "r")

# Open destination file in write mode
destination = open("sample.txt", "w")

# Read content from source file
data = source.read()

# Write content to destination file
destination.write(data)

# Close both files
source.close()
destination.close()

print("File copied successfully!")
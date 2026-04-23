#Write a program to write and append data to a file.

# 1. Writing data to a file (this will overwrite existing content)
file = open("sample.txt", "w")
file.write("Hello, I'm Durgesh\n")
file.write("This file is created using write mode.\n")
file.close()

print("Data written successfully!")

# 2. Appending data to the same file (this will add content at the end)
file = open("sample.txt", "a")
file.write("This line is added using append mode.\n")
file.write("Appending does not delete old data.\n")
file.close()

print("Data appended successfully!")
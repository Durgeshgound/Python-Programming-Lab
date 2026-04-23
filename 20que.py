#Write a program to demonstrate file pointer operations using seek().

# Open file in read mode
with open("sample.txt", "r") as file:
    
    # Read first 5 characters
    print("First 5 characters:")
    print(file.read(5))
    
    # Move pointer to beginning (position 0)
    file.seek(0)
    print("\nAfter seek(0), reading again:")
    print(file.read(5))
    
    # Move pointer to 10th byte
    file.seek(10)
    print("\nAfter seek(10), reading next 5 characters:")
    print(file.read(5))
    
    # Move pointer to end of file
    file.seek(0, 2)   # 2 means from end
    print("\nPointer moved to end of file.")
    print("Current position:", file.tell())
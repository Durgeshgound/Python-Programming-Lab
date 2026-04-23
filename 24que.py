#Write a program to handle exceptions using try-except blocks.

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    
    result = a / b
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

except ValueError:
    print("Error: Please enter valid numbers!")

except Exception as e:
    print("Some error occurred:", e)
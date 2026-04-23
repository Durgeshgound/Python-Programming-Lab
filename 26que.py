#Write a program using finally and custom exceptions.

# Custom Exception
class NegativeNumberError(Exception):
    pass

try:
    num = int(input("Enter a positive number: "))
    
    if num < 0:
        raise NegativeNumberError("Negative numbers are not allowed!")

    result = 100 / num
    print("Result:", result)

except NegativeNumberError as e:
    print("Custom Error:", e)

except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

except ValueError:
    print("Error: Invalid input!")

finally:
    print("This block always executes.")
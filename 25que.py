#Write a program demonstrating multiple exceptions handling.
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    
    lst = [10, 20, 30]
    
    print("Division:", a / b)        # May cause ZeroDivisionError
    print("List element:", lst[a])   # May cause IndexError

except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

except ValueError:
    print("Error: Invalid input! Please enter numbers only.")

except IndexError:
    print("Error: List index out of range!")

except Exception as e:
    print("Other error:", e)

finally:
    print("Program executed successfully (with or without errors).")
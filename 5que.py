#Write a program using nested if to classify a number (positive,negative, zero).

num=int(input("Ente the number :"))

if num >= 0:
    if num == 0:
        print("The number is Zero")
    else:
        print("The number is Positive")

else:
    print("Number is negative")
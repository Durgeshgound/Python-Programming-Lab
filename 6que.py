#Write a program using for loop to print multiplication table of a number.

num=int(input("Enter the number :"))

for i in range (1,11):
    print(num, "x", i, "=", num * i)

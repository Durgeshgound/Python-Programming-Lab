#Write a program using if-else to find the largest of three numbers.

x=int(input("Enter the value of x:"))
y=int(input("Enter the value of y:"))
z=int(input("Enter the value of z:"))

if(x>y&x>z):
    print(x," is a greater number")
elif(y>z&y>x):
    print(y,"is a greater number")
else:
    print(z,"is a greater number")
      

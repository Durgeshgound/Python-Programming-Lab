#Demonstrate use of break, continue, and pass in loops.

#For Break
print("For Break")
n=int(input("Enter the number:"))
for i in range (1,n):
    if(i==3):
        break
    print(i)

#For Continue
print("For continue")
n=int(input("Enter the number:"))
for i in range(1,n):
    if(i==3):
        continue
    print(i)

#For pass
print("For Pass")
n=int(input("Enter the number:"))
for i in range(1,n):
    if(i==3):
        pass
    print(i)


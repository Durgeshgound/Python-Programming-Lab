#Write a program using while loop to compute sum of first N natural numbers.

n=int(input("Enter the number:"))
sum=0
i=1
while i<=n:
    sum+=i
    i+=1
print("Sum of first N natural number =",sum)

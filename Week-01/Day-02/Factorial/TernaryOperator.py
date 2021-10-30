#find a factorial of a given number using Ternary operator

def factorial(n):
    return 1 if (n==1 or n==0) else n*factorial(n-1)

#Driver Code
n=int(input("Enter a number to find a factorial:"))
print("factorial of a given number:",factorial(n))
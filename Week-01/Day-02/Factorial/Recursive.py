#Find the factorial of a given number using Recursion

def factorial(n):
    return 1 if (n==1 or n==0) else n*factorial(n-1);

n=int(input("Enter a Integer No:"))
print("Factorial of a given number is:",factorial(n))

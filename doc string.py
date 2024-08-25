def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
print("Factorial of 5 is",factorial(5))

#Fibonacci series
#0 1 1 2 3 5 8 13......
def fibo(n):
    if (n<=0):
        print("Incorrect output")
    elif n==0:
        return 0
    elif n==1 or n==2:
        return 1
    else:
        return fibo(n-1)+ fibo(n-2)
print(fibo(9))
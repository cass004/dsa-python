def fib(n):
    if n ==0:
        return 1
    if(n==1):
        return 1
    last = fib(n-1)
    secondlast = fib(n-2)
    return last + secondlast
print(fib(4))
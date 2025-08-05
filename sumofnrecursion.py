def sumn(n):
    if(n==1):
        return 1
    smallanswer = sumn(n-1)
    return n+smallanswer
print(sumn(5))  # Output: 15
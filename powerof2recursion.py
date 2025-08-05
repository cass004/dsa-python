def power2(n):
    if(n==1): #base case
        return 2
    smallanswer = power2(n-1) #recursive call
    ans = 2*smallanswer
    return ans
print(power2(5))  

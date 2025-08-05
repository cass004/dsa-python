def onenn(n):
   if(n<=0):
      return
   print(onenn(n-1)) 
   print(n)
print(onenn(5))  # Output: 1 2 3 4 5
def sumarray(n):
   if (len(n) == 0):
      return 0
   
   sumofleftover = sumarray(n[1:])
   ans = sumofleftover +n[0]
   return ans
print(sumarray([1, 2, 3, 4, 5]))  # Output: 15
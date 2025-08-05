def lsrec(l1,x,index):
    if len(l1) == index:
        return False
    ansrecusion = lsrec(l1,x,index+1)
    if(ansrecusion==True):
        return True
    if l1[index] == x:
        return True
    return False

print(lsrec([1,2,3,4,5], 3, 0))  # Output: True
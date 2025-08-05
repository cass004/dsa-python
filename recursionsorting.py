def checksorted(lst):
    if(len(lst)==1 or len(lst)==0) :
        return True
    ans = checksorted(lst[1:])
    if(lst[0]<=lst[1]):
        return True
    else:
        return False
    
print(checksorted([1, 2, 3, 4, 5]))  # Output: True
print(checksorted([5, 4, 3, 2, 1]))
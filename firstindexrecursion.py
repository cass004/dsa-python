def firstindex(l1,x):
    if len(l1) == 0:
        return -1
    if l1[0] == x:
        return 0
    smalloutput = firstindex(l1[1:], x)
    if smalloutput == -1:
        return smalloutput
    else:
        return smalloutput + 1
print(firstindex([1, 2, 3, 4, 5], 3))  # Output: 2
print(firstindex([1, 2, 3, 4, 5], 6))  # Output: -1
print(firstindex([], 1))  # Output: -1
print(firstindex([1, 2, 3, 4, 5], 1))  # Output: 0


def returnsubsequence(s1):
    if s1 == '':
        return ['']
    
    smallans = returnsubsequence(s1[1:])
    ans = []
    
    for item in smallans:
        ans.append(item)              # without current character
        ans.append(s1[0] + item)      # with current character
    
    return ans

s1 = 'abc'
l1 = returnsubsequence(s1)
print(l1)

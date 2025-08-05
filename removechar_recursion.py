def removechar(s1,ch):
    if(len(s1) == 0 or s1 == ''):
        return s1
    smallans = removechar(s1[1:], ch)
    if s1[0] == ch:
        return smallans
    return s1[0] + smallans

print(removechar("abcbad", 'a'))  
print(removechar("hello world", 'o'))  
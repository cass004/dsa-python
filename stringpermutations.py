def printpermutations(s1,takensofar):
    if len(s1) == 0:
        print(takensofar)
        return
    
    ourchar = s1[0]
    smallinput = s1[1:]
    for i in range(0,len(takensofar) + 1):
        newstring = takensofar[:i] + ourchar + takensofar[i:]
        printpermutations(smallinput, newstring)

s1 = 'abc'
printpermutations(s1, '')
def printsubsequences(s1,takensofar):
    if(s1=='' or len(s1)==0):
        print(takensofar)
        return
    currentchar = s1[0]
    smallinput=s1[1:]
    printsubsequences(smallinput,takensofar+currentchar)
    printsubsequences(smallinput,takensofar)
    return
s1='abc' 
printsubsequences(s1,'')  

    
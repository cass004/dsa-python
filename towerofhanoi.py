def towerofhanoid(n, source, target, auxiliary):
    if(n==0):
        return
    if(n==1):
        print(source, "->", target)
    towerofhanoid(n-1,source,auxiliary,target)
    towerofhanoid(n-1,auxiliary,target,source)

towerofhanoid(3, 'A', 'C', 'B')  # A is source, C is target, B is auxiliary
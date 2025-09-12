def getchar(value):
    if value <= 0 or value > 26:
        return ''
    return chr(value + 96)  

def returnallcodes(input):
    if input == '':
        return ['']

    mainans = []

    
    singledigit = int(input[0:1])
    if 1 <= singledigit <= 9:
        answithoutfirstdigit = returnallcodes(input[1:])
        for eachans in answithoutfirstdigit:
            mainans.append(getchar(singledigit) + eachans)

    
    if len(input) >= 2:
        doubledigit = int(input[0:2])
        if 10 <= doubledigit <= 26:
            answithoutfirsttwodigits = returnallcodes(input[2:])
            for eachans in answithoutfirsttwodigits:
                mainans.append(getchar(doubledigit) + eachans)

    return mainans

ans = returnallcodes('1123')
print(ans)

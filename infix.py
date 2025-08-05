def infixtopostfix(infix):
    postfix=[]
    stack=[]
    for c in infix:
        if c.isalnum():
            postfix.append(c)
        elif c == '(':
            stack.append(c)
        elif c == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()
        else:
            while stack and precedence(c) <= precedence(stack[-1]):
                postfix.append(stack.pop())
            stack.append(c)    
    while stack:
        postfix.append(stack.pop())
    return ''.join(postfix)

def precedence(operator):
    if operator in ('+', '-'):
        return 1
    elif operator in ('*', '/'):
        return 2
    return -1


infix_expression = input()
result = infixtopostfix(infix_expression)
print(str(result))
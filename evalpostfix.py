def evaluatepostfix(postfix):
    stack = []
    for token in postfix.split():
        if is_operand(token):
            stack.append(int(token))
        else:
            operand2 = stack.pop()
            operand1=stack.pop()
            if token == "+":
                stack.append(operand1+operand2)
            elif token == "-":
                stack.append(operand1-operand2)
            elif token == "*":
                stack.append(operand1*operand2)
            elif token == "/":
                stack.append(operand1/operand2)
    return stack.pop()
def is_operand(token):
    return token.isdigit()
ip = input()
print(evaluatepostfix(ip))

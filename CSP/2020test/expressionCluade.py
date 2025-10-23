def compute():
    stack = list()
    # 在读取输入时就过滤掉空字符串
    # expression = [s for s in input().split(' ') if s]
    # 或者在循环内过滤
    for token in expression:
        if not token:
            continue
            
        if 'x' in token:
            stack.append(varVal[int(token[1:]) - 1])
        elif token == '&':
            if len(stack) < 2: raise RuntimeError("Stack underflow for &") # 防御性编程
            b = stack.pop()
            a = stack.pop()
            stack.append(1 if a == 1 and b == 1 else 0)
        elif token == '|':
            if len(stack) < 2: raise RuntimeError("Stack underflow for |") # 防御性编程
            b = stack.pop()
            a = stack.pop()
            stack.append(0 if a == 0 and b == 0 else 1)
        elif token == '!':
            if len(stack) < 1: raise RuntimeError("Stack underflow for !") # 防御性编程
            a = stack.pop()
            stack.append(1 - a)
            
    if len(stack) != 1: raise RuntimeError("Malformed expression, final stack size is not 1") # 防御性编程
    return stack[0]
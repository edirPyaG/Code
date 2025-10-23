import heapq
import sys
"""
采用栈处理后缀表达式
改值后逐个计算

"""

def main():
    #获取基本的输入信息:包含后缀表达式
    #变量值,变量调整次数,调整变量的内容
    outcome=list()
    for i in range(chaNum):#计算每次调整后的结果
        varVal[chaVar[i]-1]=abs(varVal[chaVar[i]-1]-1)#变量值取反
        outcome.append(compute())
        varVal[chaVar[i]-1]=abs(varVal[chaVar[i]-1]-1)#变量值取反
    for i in range(chaNum):
        print(outcome[i])



def compute():
    #核心处理内容
    stack=list()
    for token in expression:
        token = token.strip()
        if not token:
            continue
        # 变量形式 x1,x2,...
        if token.startswith('x'):
            try:
                idx = int(token[1:]) - 1
            except ValueError:
                raise ValueError(f"Invalid variable token: {token}")
            if idx < 0 or idx >= len(varVal):
                raise IndexError(f"Variable index out of range: {token}")
            stack.append(varVal[idx])
            continue

        # 二元运算符
        if token in ('+','-','*','/','&','|'):
            if len(stack) < 2:
                raise IndexError(f"Not enough operands for operator '{token}'")
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                # protect division by zero
                if b == 0:
                    raise ZeroDivisionError('Division by zero')
                stack.append(int(a / b))
            elif token == '|':
                stack.append(a | b)
            elif token == '&':
                stack.append(a & b)
            continue

        # 一元非运算
        if token == '!':
            if len(stack) < 1:
                raise IndexError("Not enough operands for '!' operator")
            a = stack.pop()
            stack.append(0 if a != 0 else 1)
            continue

        # 未知标记
        raise ValueError(f"Unknown token in expression: '{token}'")

    if not stack:
        raise ValueError('Empty evaluation stack; invalid expression')
    return stack[-1]  # 返回最终结果

if __name__=="__main__":
    # 支持两种读取方式：命令行传入文件名，或从 stdin 重定向读取
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as f:
            lines = [line.rstrip('\n') for line in f.readlines()]
    else:
        lines = [line.rstrip('\n') for line in sys.stdin.read().splitlines()]

    # 过滤空行
    lines = [ln for ln in lines if ln.strip() != '']
    if not lines:
        src = sys.argv[1] if len(sys.argv) > 1 else 'stdin'
        raise ValueError(f'Input is empty or only contains blank lines (source={src})')
    if len(lines) < 4:
        raise ValueError('Not enough input lines')

    # 解析输入
    expression = lines[0].split()  # 使用默认 split() 去除多余空白
    # 简单验证：后缀表达式至少应包含变量标识（如 x1）或运算符
    token_sample = set(expression)
    has_var_or_op = any(t.startswith('x') or t in ('+','-','*','/','&','|','!') for t in token_sample)
    if not has_var_or_op:
        src = sys.argv[1] if len(sys.argv) > 1 else 'stdin'
        raise ValueError(f"Input format mismatch: first line (source={src}) doesn't look like a postfix expression. Got tokens: {expression[:10]}{'...' if len(expression)>10 else ''}")
    varNum = int(lines[1].strip())
    varVal = list(map(int, lines[2].split()))
    chaNum = int(lines[3].strip())
    chaVar = []
    expected = 4 + chaNum
    if len(lines) < expected:
        raise ValueError('Not enough lines for change indices')
    for i in range(4, 4 + chaNum):
        chaVar.append(int(lines[i].strip()))

    try:
        main()
    except Exception as e:
        # 把错误信息更友好地展示出来，便于定位输入格式或运行时问题
        print(f"Error during execution: {e}", file=sys.stderr)
        raise
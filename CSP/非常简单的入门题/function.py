import sys

# 增加递归深度限制，以防万一
sys.setrecursionlimit(10**6)

# 1. 正确初始化记忆化数组
# 尺寸为 21x21x21 以存储 (0,0,0) 到 (20,20,20) 的结果
# 使用列表推导式创建独立的对象
memo = [[[None for _ in range(21)] for _ in range(21)] for _ in range(21)]

# 2. 将 w 定义为一个独立的函数，而不是类的方法
def w(a, b, c):
    # 基础情况1：a,b,c <= 0
    if a <= 0 or b <= 0 or c <= 0:
        return 1

    # 基础情况2：a,b,c > 20
    # 题目规定 w(a,b,c) = w(20,20,20) 如果 a>20 或 b>20 或 c>20
    # 所以我们直接在函数调用层面处理，或者在递归内部截断
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)

    # 3. 检查记忆化数组中是否已有结果
    if memo[a][b][c] is not None:
        return memo[a][b][c]

    # 4. 根据题目条件进行递归计算
    result = 0
    if a < b and b < c:
        result = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
    else:
        result = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
    
    # 5. 将计算结果存入记忆化数组
    memo[a][b][c] = result
    return result

if __name__ == "__main__":
    while True:
        try:
            # 读取一行输入
            line = input()
            a, b, c = map(int, line.split())

            # 结束条件
            if a == -1 and b == -1 and c == -1:
                break
            
            # 调用修正后的 w 函数
            ans = w(a, b, c)
            
            # 按格式输出
            # 注意原始输入的 a,b,c 可能和实际计算的不同 (例如 a>20)，但输出时要用原始值
            print(f"w({a}, {b}, {c}) = {ans}")

        except EOFError:
            # 处理没有输入或输入结束的情况
            break


































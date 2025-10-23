import sys
sys.setrecursionlimit(10000)

solCount = 0
side = 0 # 将 side 提升为全局变量，以便在 dfs 中访问

def dfs(row, colUsed, mainDiagUsed, antiDiagUsed, solution):
    """
    row: 当前处理的行号 (0-based)
    ...
    solution: 存储当前路径解的列表 (0-based)
    """
    global solCount
    
    # 递归退出条件：成功放置了 side 行的皇后
    if row == side:
        solCount += 1
        if solCount <= 3:
            # 修正4: 输出时将 0-based 的解转换为 1-based
            # 例如 [1, 3, 5, 0, 2, 4] -> 2 4 6 1 3 5
            print(' '.join(map(str, [s + 1 for s in solution])))
        return
        
    # 遍历当前行的每一列
    for col in range(side):
        # 修正1: 关键的检查步骤！判断 (row, col) 是否安全
        is_col_safe = not colUsed[col]
        # 主对角线 (row - col) 恒定, 偏移量 side-1 保证索引非负
        is_main_diag_safe = not antiDiagUsed[row - col + side - 1]
        # 副对角线 (row + col) 恒定
        is_anti_diag_safe = not mainDiagUsed[row + col]
        
        if is_col_safe and is_main_diag_safe and is_anti_diag_safe:
            # --- 放置棋子 (标记) ---
            solution.append(col)
            # 修正2: 使用正确的索引 col
            colUsed[col] = True
            mainDiagUsed[row + col] = True
            antiDiagUsed[row - col + side - 1] = True
            
            # --- 递归到下一行 ---
            dfs(row + 1, colUsed, mainDiagUsed, antiDiagUsed, solution)
            
            # --- 回溯 (撤销标记) ---
            # 修正3: 对 solution 列表进行回溯
            solution.pop()
            colUsed[col] = False
            mainDiagUsed[row + col] = False
            antiDiagUsed[row - col + side - 1] = False

def main():
    global side # 声明要修改全局变量 side
    try:
        side = int(input())
    except (ValueError, EOFError):
        return

    solution = list()
    # 标记数组大小要正确
    colUsed = [False] * side
    mainDiagUsed = [False] * (2 * side - 1)
    antiDiagUsed = [False] * (2 * side - 1)
    
    dfs(0, colUsed, mainDiagUsed, antiDiagUsed, solution)
    
    print(solCount)

if __name__ == "__main__":
    main()
"""
经典搜索问题,用到递归和回溯
进行深度递归,标记使用位
找到一个解后,回溯,进一步找下一个解

"""
import sys
sys.setrecursionlimit(10000)
solCount=0
def dfs(row,colUsed,mainDiagUsed,antiDiagUsed,solution):
    global solCount
    #考虑退出条件
    if row==side:
        solCount+=1
        if solCount<=3:
            print(*solution)
        return
    for col in range(side):
        colUsed[row]=True
        mainDiagUsed[row+col]=True
        antiDiagUsed[row-col+side-1]=True
        solution.append(col)
        dfs(row+1,colUsed=colUsed,mainDiagUsed=mainDiagUsed,antiDiagUsed=antiDiagUsed,solution=solution
            )
        colUsed[row]=False
        mainDiagUsed[row+col]=False
        antiDiagUsed[row-col+side-1]=False

"""
定义处理主要逻辑
"""
def main():
    solution=list()
    colUsed=list(False for _ in range(side))
    mainDiagUsed=list(False for _ in range(2*side-1))
    antiDiagUsed=list(False for _ in range(2*side-1))
    dfs(0,colUsed,mainDiagUsed,antiDiagUsed,solution)
    print(solCount)

if __name__=="__main__":
    """
    约束抽象化为:列值不相同, 主对角线和副对角线约束
    """
    side=int(input())

    main()
    



















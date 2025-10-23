"""
数字的划分
动态规划问题
关键是找到状态转移方程,如何将当前状态划分为几个互斥的子状态
在这之前,首先要先将介个变量参数化
"""
n,k=map(int,input().split())

#建立记忆表
dp=[[0 for _ in range(k+1)] for _ in range(n+1)]

#状态转移方程:
#dp[i][j]=dp[i-j][j]+dp[i-1][j-1]
#dp[i][j]表示将i划分为j个正整数的方案数

for i in range(1,n+1):
    for j in range(1,min(i,k)+1):
        if i==j:
            dp[i][j]=1
        elif j==1:
            dp[i][j]=1
        else:
            dp[i][j]=dp[i-j][j]+dp[i-1][j-1]
print(dp[n][k])







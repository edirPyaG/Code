M=int(input())

#初始化斐波那契数列的记忆表

fibMemo=[0 for _ in range(0,M**2)]

fibMemo[0]=0
fibMemo[1]=1
fibMemo[2]=1
def fib(n):
    #退出条件
    if n==1 or n==0 or n==2:
        return fibMemo[n]
    if fibMemo[n]!=0:
        return fibMemo[n]
    #递规进行计算
    fibMemo[n]=fib(n-1)+fib(n-2)
    return fibMemo[n]

fib(M**2-1)
for i in range(2,M**2):
    if fibMemo[i]%M==0 and fibMemo[i+1]%M==1:
        print(i)
        break


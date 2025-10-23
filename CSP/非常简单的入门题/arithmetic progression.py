#用记忆表法来降低复杂度
a1,a2,n=map(int , input().split())
d=a2-a1
memSum=[-1 for i in range(n)]
memit=[-1 for i in range(n)]
for i in range(n):
    if i==0:
        memit[0]=a1
    else:
        memit[i]=memit[i-1]+d
def SumarithProg(a1,a2,d,n):#这里的n表示当前计算到的第n项
    if n==1:
        return a1
    elif n==2:
        return a1+a2
    else:
        if memSum[n-1]==-1:
            memSum[n-1]=SumarithProg(a1,a2,d,n-1)+ memit[n-1]
            return memSum[n-1]
        else:
            return memSum[n-1]
print(SumarithProg(a1,a2,d,n))




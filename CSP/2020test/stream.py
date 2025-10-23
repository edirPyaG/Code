#输入
n,w = map(int,input().split())
grade= list(map(int,input().split()))

#输出
baseline=list()
baseNum=0
for m in range(n):
    m=m+1
    temp=grade[0:m:1]
    baseNum=max(1, int((m)*(w/100)))
    for i in range(m):
        for j in range(m-i-1):
            if temp[j+1]>temp[j]:
                temp[j+1],temp[j]=temp[j],temp[j+1]
    baseline.append(temp[baseNum-1])
print(*baseline)
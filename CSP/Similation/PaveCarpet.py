#这是铺地毯问题

#输入
n = int(input())
carpets=[[0 for _ in range(4)] for _ in range(n)]
for i in range(n):
    carpets[i]=list(map(int,input().split()))
x,y=map(int,input().split())

#判断点在哪里
flag=[0 for _ in range(n)]
for i in range(n):
    if carpets[i][0]<=x<=carpets[i][2]+carpets[i][0] and carpets[i][1]<=y<=carpets[i][3]+carpets[i][1]:
        flag[i]=1

for i in range(n-1,-1,-1):
    if flag[i]==1:
        print(i+1)
        break
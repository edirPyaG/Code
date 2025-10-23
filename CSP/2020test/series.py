n=int(input())
series=1
k=2
while(1):
    if series>n:
        break
    series=series+1/k
    k=k+1
print(k-1)
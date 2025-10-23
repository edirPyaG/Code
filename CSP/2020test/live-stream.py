import sys
import heapq

def main():

    #输入n,w,和n个分数
    sumNum, percent= map(int, input().split())
    grade= list(map(int,input().split()))

    #通过小根堆维护前k个数;

    winStu=list()
    loseStu=list()

    for i in range(sumNum):
        k=max(1,int((i+1)*percent/100))
        temp=grade[i]
        #将新值放入小根堆(判断是放入小根堆还是大根堆)
        if not winStu or temp>=winStu[0]:
            heapq.heappush(winStu, temp)
        else:
            heapq.heappush(loseStu, -temp)
        #调整两个堆的大小
        while  len(winStu)>k:
            pop_temp=heapq.heappop(winStu)
            heapq.heappush(loseStu,-pop_temp)
        while len(winStu)<k and loseStu:
            pop_temp=-heapq.heappop(loseStu)
            heapq.heappush(winStu,pop_temp)

        print(winStu[0],end=" ")

if __name__=="__main__":
    main()

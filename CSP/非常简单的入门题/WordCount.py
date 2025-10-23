"""
统计单词数量
"""
import sys
target=input().lower()
text=sys.stdin.read()

text=text.lower()
textSplit=text.split()
count=textSplit.count(target)

if count!=0:
    print(count,end=' ')
    print(text.find(target))
else:
    print(-1)

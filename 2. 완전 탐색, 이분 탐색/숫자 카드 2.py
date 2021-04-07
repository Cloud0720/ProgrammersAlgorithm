from collections import Counter

N = int(input())
numbers = list(map(int,input().split()))
M = int(input())
match = list(map(int,input().split()))


answer = Counter(numbers)
    
for i in match:
    print(answer[i], end=' ')

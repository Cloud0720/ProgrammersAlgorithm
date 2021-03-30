def solution(prices):
    answer = []
    for i in range(len(prices)):
        k=0
        for j in range(i+1,len(prices)):
            k+=1
            if(prices[j] < prices[i]):
                break
                
        answer.append(k)    
    return answer

prices=[1,2,3,2,3]
print(solution(prices))
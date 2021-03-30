def solution(progresses, speeds):
    answer = []
    before = 0
    i = 0

    for i in range(len(progresses)):
        temp = 100 - progresses[i] 
        temp = round(temp / speeds[i])

        if(before < temp):
            answer.append(1)
            before = temp
            i += 1  
            
        else:
            answer[i-1] += 1      

    return answer


result = solution([93, 30, 55], [1, 30, 5])
print(result)
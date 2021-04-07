def solution(answers):
    answer = []
    no1 = [1,2,3,4,5]
    no2 = [2,1,2,3,2,4,2,5]
    no3 = [3,3,1,1,2,2,4,4,5,5]

    count = [0,0,0]
    
    for i in range(len(answers)):
            
        if( answers[i] == no1[i%5]):  count[0]+=1
        if( answers[i] == no2[i%8]):  count[1]+=1
        if( answers[i] == no3[i%10]): count[2]+=1

ㄴ
    for student, score in enumerate(count): 
        if score == max(count): answer.append(student+1)



    return answer

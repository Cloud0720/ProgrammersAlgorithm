def solution(bridge_length, weight, truck_weights):
    q = [0] * bridge_length
    time = 0
    while len(q) != 0:
        time+=1
        q.pop(0)
        if truck_weights:
            if sum(q) + truck_weights[0] <= weight:
                q.append(truck_weights.pop(0))
            else:
                q.append(0)
                
    return time

result = solution(2,10,[7,4,5,6])
print(result)
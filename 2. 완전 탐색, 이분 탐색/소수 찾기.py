from itertools import permutations
import math

def isPrime(n):
    j = math.sqrt(n)
    if n < 2: 
        return False

    for i in range(2, int(j)+1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    answer = []
    for j in range(1, len(numbers)+1):
        perlist = map(int, list(map(''.join, permutations(list(numbers), j))))
        for i in list(set(perlist)):
            if isPrime(i):
                answer.append(i)

    answer = len(set(answer))

    return answer


from collections import deque

def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    sum_of_q1 = sum(q1)
    sum_of_q2 = sum(q2)
    half = (sum_of_q1 + sum_of_q2)//2
    count = 0
    
    while q1 and q2:
        if sum_of_q1 < half:
            x = q2.popleft()
            sum_of_q1 += x
            q1.append(x)
            count += 1
            
        elif sum_of_q1 > half:
            sum_of_q1 -= q1.popleft()
            count += 1
        else:
            return count
            
        """sum_of_q1 = sum(q1)
        sum_of_q2 = sum(q2)"""
    else:
        return -1
        

solution([3,2,7,2], [4,6,5,1])
def solution(numbers):
    answer = 0
    num = [1,2,3,4,5,6,7,8,9,0]
    sub_num = list(set(num) - set(numbers))
    cnt = 0
    for i in sub_num:
        answer = sub_num[cnt] + answer
        cnt += 1
    return answer
    
"""
numbers라는 매개변수에 0~9까지의 수가 한개씩 랜덤하게 들어오는데 이 numbers안에 없는 수를 찾아서 다 더하여라
"""

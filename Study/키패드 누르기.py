def solution(numbers, hand):
    answer = ''
    keypad = {1:[0,0], 2:[0,1], 3:[0,2],
             4:[1,0], 5:[1,1],6:[1,2],
              7:[2,0], 8:[2,1], 9:[2,2],
              "*":[3,0], 0:[3,1], "#":[3,2]
             }
    left_first = keypad["*"] #왼손의 현재위치
    right_first = keypad["#"] # 오른손의 현재위치

    # 1, 4, 7이면 무조건 L
    for i in numbers:
        now = keypad[i]
        if i in [1,4,7]:
            answer = answer + "L"
            left_first = now 
            # 3, 6, 9이면 무조건 R
        elif i in [3,6,9]: 
            answer += "R"
            right_first = now
            # 2, 5, 8, 0을 누를 때
        else:
            left_dist = 0
            right_dist = 0
            # 좌표 거리 계산해주기
            for a, b, c in zip(left_first, right_first, now):
                left_dist += abs(a-c)
                right_dist += abs(b-c)
                # 왼손이 더 가까울 때
            if left_dist < right_dist:
                answer += 'L'
                left_first = now
                # 오른손이 더 가까울 때
            elif left_dist > right_dist:
                answer += 'R'
                right_first = now
                # 두 거리가 같을 때
            else:
              # 왼손잡이
                if hand == 'left':
                    answer += 'L'
                    left_first = now
              # 오른손 잡이
                else:
                    answer += 'R'
                    right_first = now
    
    return answer

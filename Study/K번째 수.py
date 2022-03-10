def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        cnt = 0
        k_list=array[commands[i][0]-1:commands[i][1]]
        k_list.sort()
        answer.append(k_list[commands[i][2]-1])
    return answer

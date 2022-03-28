# 실제 답 
def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    
    for i ,j in zip(participant, completion):
        if i != j:
            return i
    
    return participant.pop()
  
  
  
  
  
  # 내가 생각한 답
 """
  def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    
    for i in range(len(participant)):
      for j in range(len(completion)):
        if participant[i] == completion[j]:   # 정렬해놓은 배열값이 다르면 제거해서 for문이 다 돌면 participant안에는 완주하지 못한 선수만 남아있게 만들었다(라고 생각했다.)
          participant.remove(participant[i])
        answer.append(participant[i])
    
    return answer
  """
  
  
  
  
  

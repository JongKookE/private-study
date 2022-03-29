"""1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
     만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.

처음으로 제대로 코딩 테스트 문제를 풀어봤는데 생각보다 꽤 많이 헤매었다. 
많이 힘들었던게 .을 연속으로 처리하는 부분의 변수를 new_id말고 다른 걸로 했었다가 왠지 모르겠지만 자꾸 안먹어서 계속 씨름만 하다가 결국엔 new_id로 바꿔서 풀었더니 바로
해결되서 많이 허무했었다...
"""

def solution(new_id):
    new_id = new_id.lower() #모두 소문자로 바꿈
    # "_", "-", ".", 알파벳, 숫자를 제외한 모든 문자는 삭제
    replace_item = "~`!@#$%^&*\"()\'+:\;<>,/?={}[]|" 
    for x in range(len(replace_item)):
        new_id = new_id.replace(replace_item[x],"")   
   
   # "."이 2번 이상 나오면 "."로 치환 
    for i in range(len(new_id)):
        new_id= new_id.replace("..",".") 
    
    # 문자열의 처음과 끝이 "."라면 삭제
    if new_id[0] == ".":
        new_id = new_id[1:]
    if new_id[:len(new_id)] == ".":
        new_id = new_id[:-1]
    
    # 빈 리스트인지 확인하고 빈 리스트라면 "a" 넣어주고 문자열의 최대 길이를 15로 제한
    if not new_id:
        new_id = 'a'
    else:
        new_id = new_id[:15]
        
     #15로 제한된 문자열의 끝이 "."라면 삭제   
    if new_id[-1] == ".":
        new_id = new_id[:-1]
    else:
        pass
        
        # new_id의 길이가 3보다 작으면 3이 될때까지 문자열의 마지막 문자를 반복해줌
    if len(new_id) <= 2:
        while len(new_id) != 3:
            new_id = new_id + new_id[-1]
            
    return new_id

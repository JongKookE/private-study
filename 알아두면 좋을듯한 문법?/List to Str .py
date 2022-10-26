def listToString(str_list):
    result = ""
    for s in report:
        result += s+""
    return result.strip()
    
    
str_list = ['This', 'is', 'a', 'python tutorial']
result = listToString(str_list)
print(result)

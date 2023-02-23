def solution(s):    
    lst = []
    for c in s:
        if c == "(":
            lst.append(c)
        else:
            if lst:
                lst.pop()
            else:
                return False
    if lst:
        return False

    return True
    
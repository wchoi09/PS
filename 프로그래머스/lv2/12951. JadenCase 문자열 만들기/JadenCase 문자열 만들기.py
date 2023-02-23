def solution(s):
    answer = ""
    tmp_lst = [x.capitalize() for x in s.split(" ")]
    answer = " ".join(tmp_lst)
    return answer

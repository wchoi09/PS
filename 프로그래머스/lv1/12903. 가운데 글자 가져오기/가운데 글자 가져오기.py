def solution(s):
    num_char = len(s)
    answer = s[(num_char - 1) // 2 : (num_char // 2) + 1]

    return answer

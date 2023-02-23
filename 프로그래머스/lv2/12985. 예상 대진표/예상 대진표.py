def solution(N, a, b):
    a, b = (a + 1) // 2, (b + 1) // 2

    if a == b:
        return 1

    return 1 + solution(N, a, b)

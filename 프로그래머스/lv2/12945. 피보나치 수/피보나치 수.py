def solution(n):
    if n <= 1:
        return n

    f = [0 for i in range(n + 1)]
    f[0], f[1] = 0, 1

    for i in range(2, n + 1):
        f[i] = (f[i - 2] + f[i - 1]) % 1234567

    return f[n]

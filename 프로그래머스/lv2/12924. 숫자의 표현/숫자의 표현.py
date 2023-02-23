def solution(n):
    cnt = 1

    for i in range(1, ((n + 1) // 2) + 1):
        cur = 0
        for j in range(i, n):
            if cur + j <= n:
                cur += j
                if cur == n:
                    cnt += 1
                    break
            else:
                break

    return cnt

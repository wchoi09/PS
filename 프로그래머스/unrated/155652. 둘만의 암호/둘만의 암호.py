def solution(s, skip, index):
    alphabet = [chr(i) for i in range(ord("a"), ord("z") + 1) if chr(i) not in skip]

    answer = ""
    for c in s:
        idx = (alphabet.index(c) + index) % len(alphabet)
        answer += alphabet[idx]

    return answer

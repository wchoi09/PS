def dec2bin(dec):
    bin = ""
    while dec != 0:
        bin = f"{dec %2}{bin}"
        dec = dec // 2
    return bin

def solution(s):
    cnt = 0
    num_zero = 0

    while s != "1":
        cnt += 1
        num_zero += s.count("0")
        s_len = len(s.replace("0", ""))
        s = str(dec2bin(s_len))
    return [cnt, num_zero]

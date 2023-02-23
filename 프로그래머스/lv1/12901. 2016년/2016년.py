def solution(a, b):
    last_day = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day_dict = {3: "SUN", 4: "MON", 5: "TUE", 6: "WED", 0: "THU", 1: "FRI", 2: "SAT"}
    date_days = sum(last_day[: a - 1]) + b
    answer = day_dict[date_days % 7]
    return answer
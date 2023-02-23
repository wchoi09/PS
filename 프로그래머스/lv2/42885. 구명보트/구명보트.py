def solution(people, limit):
    num_boat = len(people)
    people = sorted(people)
    start_idx = 0
    end_idx = len(people) - 1
    while start_idx < end_idx:
        if people[start_idx] + people[end_idx] <= limit:
            start_idx += 1
            end_idx -= 1
            num_boat -= 1

        else:
            end_idx -= 1

    return num_boat

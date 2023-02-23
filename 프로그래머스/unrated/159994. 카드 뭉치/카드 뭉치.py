def solution(cards1, cards2, goal):
    for x in goal[:]:
        if cards1 and cards1[0] == x:
            cards1.pop(0)
            goal.pop(0)

        elif cards2 and cards2[0] == x:
            cards2.pop(0)
            goal.pop(0)

    if not goal:
        return "Yes"
    else:
        return "No"
    
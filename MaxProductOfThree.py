def solution(A):
    outofrange = 10 ** 3 + 1
    maxThree = 3 * [-outofrange]
    minTwo = 2 * [outofrange]

    for elem in A:
        if elem >= maxThree[0]:
            maxThree[2] = maxThree[1]
            maxThree[1] = maxThree[0]
            maxThree[0] = elem
        elif elem >= maxThree[1]:
            maxThree[2] = maxThree[1]
            maxThree[1] = elem
        elif elem >= maxThree[2]:
            maxThree[2] = elem

        if elem <= minTwo[1]:
            minTwo[0] = minTwo[1]
            minTwo[1] = elem
        elif elem <= minTwo[0]:
            minTwo[0] = elem

    combo_top = maxThree[0] * maxThree[1] * maxThree[2]
    combo_bottom = maxThree[0] * minTwo[0] * minTwo[1]

    if combo_top > combo_bottom:
        return combo_top
    else:
        return combo_bottom

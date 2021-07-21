import math

def solution(n):
    m = int(n)
    lg_m = math.log(m, 2)

    if lg_m.is_integer():
        return int(lg_m)

    c = 0

    while m > 1:
        if m % 2 == 0:
            m /= 2
            c += 1
        elif m % 4 == 1 or m == 3:
            m -= 1
            m /= 2
            c += 2
        else:
            m += 1
            m /= 2
            c += 2

    return c
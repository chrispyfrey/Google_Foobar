def solution(h, q):
    rt = (2**h) - 1
    y = []

    for qn in q:
        if qn <= rt - 1:
            hm = h - 1
            yn = rt

            if qn == yn - 2**hm or qn == yn - 1:
                y.append(yn)
                yn = -1

            while yn > 0:
                if qn <= yn - 2**hm:
                    yn -= 2**hm
                    hm -= 1
                else:
                    yn -= 1
                    hm -= 1

                if qn == yn - 2**hm or qn == yn - 1:
                    y.append(yn)
                    break
        else:
            y.append(-1)
    
    return y

#########################
#          Main
#########################
p = solution(6, [4, 42, 16])
print(p)
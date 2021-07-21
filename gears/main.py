import random

def solution(pegs):
    p_num = len(pegs)
    is_evn = not p_num % 2
    d = 0

    for i in range(p_num - 1):
        dn = pegs[i+1] - pegs[i]

        if dn < 2:
            return [-1, -1]

        if is_evn & i % 2:
            d += dn
        elif not is_evn and not (i % 2):
            d += dn

    l = pegs[-1] - pegs[0]
    r = (2*l) - (4*d) if is_evn else (12*d) - (6*l)

    if r < 6 or r > 3*(pegs[1] - pegs[0] - 1):
        return [-1, -1]

    lr = r

    for i in range(p_num - 1):
        dn = pegs[i+1] - pegs[i]
        lr = (3 * dn) - lr

        if lr < 3 or lr > 3*(dn - 1):
            return [-1, -1]

    r_scaled = float(r) / float(3)

    if r_scaled.is_integer():
        return [int(r_scaled), 1]
    else:
        return [r, 3]

#########################
#          Main
#########################
peg_num = random.randint(2, 20)
pegs = []
minimum = 0

for i in range(peg_num):
    pegs.append(random.randint(minimum + 1, 500 * (i + 1)))
    minimum = pegs[i]

radius = solution(pegs)

print(pegs)
print(radius)
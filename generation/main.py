def solution(x, y):
    m = int(x)
    f = int(y)
    c = 0

    while m > 0 and f > 0:
        if m == f:
            break

        elif m > f:
            z = float(m) / float(f)
            z = int(z) - 1 if z.is_integer() else int(z)
            m -= z*f if z > 0 else f

        else:
            z = float(f) / float(m)
            z = int(z) - 1 if z.is_integer() else int(z)
            f -= z*m if z > 0 else m
            
        c += z if z > 0 else 1

    if m == 1 and f == 1:
        return str(c)
    
    return "impossible"

print(solution('4', '7'))
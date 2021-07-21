def solution(n):
    vec = [1, 1, 1, 1]

    for i in range(n-3):
        vec.append(0)

    for i in range(3, n):
        nxt_vec = vec[:]

        for j in range(n-i+1):
            nxt_vec[i+j] += vec[j]

        vec = nxt_vec

    return vec[-1]


print(solution(200))

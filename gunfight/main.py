def solution(d, s, g, l):
    min_x, max_x = -s[0], d[0] - s[0]
    min_y, max_y = -s[1], d[1] - s[1]
    tar_x, tar_y = g[0] - s[0], g[1] - s[1]



solution([3,2], [1,1], [2,1], 4)
def solution(n):
    mem = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    mem[0][0] = 1

    for height in range(1, n + 1):
        for left in range(0, n + 1):
            # adding 1 brick to previous step
            mem[height][left] = mem[height - 1][left]
            if left >= height:
                # plus if more bricks left
                mem[height][left] += mem[height - 1][left - height]

    return mem[n][n] - 1


print(solution(7))

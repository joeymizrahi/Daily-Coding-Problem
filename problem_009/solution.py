def solution(l):
    max_2 = max(l)
    if len(l) <= 2:
        return max_2

    memory = [0] * len(l)
    memory[0] = l[0]
    memory[1] = max_2

    for i in range(2, len(l)):
        memory[i] = max(l[i] + memory[i-2], memory[i-1])

    return memory[-1]


print(solution([2, 4, 6, 2, 5]))

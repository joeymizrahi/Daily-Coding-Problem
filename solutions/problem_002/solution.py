"""Given an array of integers, return a new array such that:
each element at index i of the new array is the product of all the numbers
in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], 
the expected output would be [120, 60, 40, 30, 24]. 
If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?"""


def solution(l):
    result = [1]*len(l)
    past = [1]*len(l)
    future = [1]*len(l)
    for i, _ in enumerate(l[1:]):
        past[i+1] = past[i] * l[i]
    for i in range(len(l)-2, -1, -1):
        future[i] = future[i + 1] * l[i + 1]

    for i, (a, b) in enumerate(zip(past, future)):
        result[i] = a*b
    return result


assert solution([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
assert (solution([3, 2, 1])) == [2, 3, 6]
